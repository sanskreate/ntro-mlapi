import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess dataset
df = pd.read_csv("dataset_sales/amazon.csv")
df = df.drop(columns=['user_id', 'user_name', 'review_id', 'review_title', 'review_content', 'img_link', 'product_link', 'rating_count'])
df.rename(columns={'about_product': 'product_description'}, inplace=True)

# Function to find similar products
def find_similar_products(user_input, top_n=5):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['product_description'])
    input_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(input_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[::-1][:top_n]
    similar_products = df.iloc[top_indices].copy()
    similar_products['similarity_score'] = similarities[top_indices]
    return similar_products
