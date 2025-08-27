from rapidfuzz import fuzz
import json
import pandas as pd
from difflib import SequenceMatcher

with open("dataset_sales/data.json", "r") as file:
    try:
        data = json.load(file)
        print("JSON is valid.")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")

# Normalize JSON data to create a DataFrame
df = pd.json_normalize(data)

# Filter all specification-related columns
spec_columns = [col for col in df.columns if col.startswith("specifications.")]
specifications_df = df[spec_columns]


# flatten specifications into a single dictionary
def flatten_specifications(row):
    return {
        col.replace("specifications.", "").lower(): row[col]
        for col in spec_columns
        if pd.notnull(row[col])  # Exclude NaN values
    }

# Add flattened specifications column
df["specifications"] = df.apply(flatten_specifications, axis=1)

# Extract specifications into a consistent format
df["specifications"] = df["specifications"].apply(lambda specs: {k.lower(): v.lower() for k, v in specs.items()})

# Function to find similar products based on specifications
def find_similar_products(user_specs, top_n=5):
    def calculate_match_score(product_specs, user_specs):
        match_count = sum(1 for k, v in user_specs.items() if product_specs.get(k) == v)
        return match_count / len(user_specs) if user_specs else 0

    df["match_score"] = df["specifications"].apply(lambda specs: calculate_match_score(specs, user_specs))
    matched_products = df[df["match_score"] > 0].nlargest(top_n, "match_score").copy()
    return matched_products[["name", "specifications", "currentPrice", "match_score"]]