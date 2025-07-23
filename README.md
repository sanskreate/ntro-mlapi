# 🛍️ Product Specification Matching API

This project offers a FastAPI-based backend to match user-specified product features against a dataset using intelligent fuzzy string matching. Ideal for e-commerce, inventory filtering, or personalized search experiences.

## 🚀 Features

- **Product Matching**: Find products most relevant to user-defined specifications.
- **Fuzzy Matching**: Uses `rapidfuzz` for flexible string comparisons—handles typos, synonyms, and partial matches.
- **FastAPI**: Lightweight, high-performance framework with auto-generated interactive documentation.
- **Data Normalization**: Converts nested JSON product specs into a searchable `pandas` DataFrame.

## 📦 Prerequisites

Make sure you have:

- Python 3.8+
- `pip` (Python package manager)

## 🛠️ Installation

```bash
git clone <repo-url>
cd <repo-directory>
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Or manually install:

```bash
pip install fastapi uvicorn pandas rapidfuzz
```

## 📁 Project Structure

```
.
├── main.py              # FastAPI app and endpoints
├── specsmatch.py        # Fuzzy matching logic
├── schemas.py           # Pydantic models (e.g., MatchRequest)
└── dataset_sales/
    └── data.json        # Product data
```

## 📚 API Usage

### 1️⃣ Run Server

```bash
uvicorn main:app --host 127.0.0.1 --port 9000 --reload
```

### 2️⃣ Open Docs

Visit [http://127.0.0.1:9000/docs](http://127.0.0.1:9000/docs) for interactive Swagger UI.

### 3️⃣ Try Endpoints

**GET /**  
Returns a welcome message.

**POST /match-products**  
Returns matching products based on your input specs.

#### Sample Request

```json
{
  "specifications": {
    "color": "red",
    "size": "large"
  },
  "top_n": 5
}
```

#### Sample Response

```json
{
  "user_input": {
    "color": "red",
    "size": "large"
  },
  "matched_products": [
    {
      "name": "License Free Walkie Talkie 6km Range",
      "specifications": {
        "color": "black",
        "size": "large"
      },
      "currentPrice": 7500.0,
      "match_score": 0.5
    },
    ...
  ]
}
```

## ⚠️ Error Handling

- `404`: No matching products found.
- `422`: Invalid request schema.
- `500`: Server error.

---
