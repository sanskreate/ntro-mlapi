
# 🛍️ Product Specification Matching API

**Product Specification Matching API** is a FastAPI-based backend that matches user-specified product features against a dataset using intelligent fuzzy string matching. It is ideal for e-commerce, inventory filtering, or personalized search experiences.

---

## 📝 Quick Start


1. **Install dependencies**
  ```powershell
  pip install -r requirements.txt
  ```
2. **Run the server**
  ```powershell
  python main.py
  ```
  The server will start on port 8000 by default.
   
  Optionally, you can use Uvicorn for auto-reload:
  ```powershell
  uvicorn main:app --host 127.0.0.1 --port 8000 --reload
  ```
3. **Open API docs**
  - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---


## 🚀 Features

- **Product Matching**: Find products most relevant to user-defined specifications.
- **Fuzzy Matching**: Uses `rapidfuzz` for flexible string comparisons—handles typos, synonyms, and partial matches.
- **FastAPI**: Lightweight, high-performance framework with auto-generated interactive documentation.
- **Data Normalization**: Converts nested JSON product specs into a searchable `pandas` DataFrame.

---


## 📦 Prerequisites

- Python 3.8+
- `pip` (Python package manager)

---


## 🛠️ Installation

```powershell
git clone <repo-url>
cd <repo-directory>
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

Or manually install:

```powershell
pip install fastapi uvicorn pandas rapidfuzz
```

---


## 📁 Project Structure

```
.
├── main.py              # FastAPI app and endpoints
├── specsmatch.py        # Fuzzy matching logic
├── schemas.py           # Pydantic models (e.g., MatchRequest)
└── dataset_sales/
  └── data.json        # Product data
```

---


## 📚 API Usage


### Endpoints

- **GET /**
  - Returns a welcome message.

- **POST /match-products**
  - Returns matching products based on your input specs.

#### Example Request (curl)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/match-products' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "specifications": {
    "ram": "8 gb",
    "storage": "128 gb",
    "brand": "acer"
  },
  "top_n": 5
}'
```

#### Example Response

```json
{
  "user_input": {
    "ram": "8 gb",
    "storage": "128 gb",
    "brand": "acer"
  },
  "matched_products": [
    {
      "name": "Acer S2670G Desktop Computer",
      "specifications": {
        "processor": "core i5",
        "color": "black",
        "model name/number": "s2670g",
        "warranty": "3 years",
        "hard drive size": "256 gb",
        "screen size": "18.5 inches",
        "ram": "8 gb",
        "brand": "acer",
        "operating system": "windows 10",
        "usage/application": "business use",
        "form factor": "all in one"
      },
      "currentPrice": 49000,
      "match_score": 0.6666666666666666
    },
    {
      "name": "RefurbishedDell Latitude Laptop 5400",
      "specifications": {
        "processor": "core i5",
        "hard drive size": "1 tb",
        "screen size": "15.6 inches",
        "ram": "8 gb",
        "brand": "dell",
        "operating system": "windows 11"
      },
      "currentPrice": 12000,
      "match_score": 0.3333333333333333
    },
    {
      "name": "Refurbished Laptop",
      "specifications": {
        "processor": "core i5",
        "color": "black silver",
        "warranty": "1 month",
        "hard drive size": "256 gb",
        "screen size": "14 inches",
        "ram": "8 gb",
        "brand": "hp",
        "operating system": "windows 11",
        "battery backup": "2 hours",
        "series": "7000,3000,x390,54000",
        "weight": "1.5"
      },
      "currentPrice": 20000,
      "match_score": 0.3333333333333333
    },
    {
      "name": "Hp Tiny Pc",
      "specifications": {
        "processor": "core i5",
        "hard drive size": "256 gb",
        "ram": "8 gb",
        "operating system": "windows 10",
        "form factor": "mini"
      },
      "currentPrice": 9900,
      "match_score": 0.3333333333333333
    },
    {
      "name": "Hp Elitebook 840 G6",
      "specifications": {
        "processor": "core i5",
        "color": "silver",
        "model name/number": "hp elitebook 840 g6",
        "hard drive size": "256 gb",
        "screen size": "14 inches",
        "ram": "8 gb",
        "operating system": "windows 11",
        "battery backup": "3 hours",
        "series": "elitebook",
        "weight": "lightwieght",
        "usage/application": "business use",
        "graphic card": "intel"
      },
      "currentPrice": 22500,
      "match_score": 0.3333333333333333
    }
  ]
}
```

---


## ⚠️ Error Handling

- `404`: No matching products found.
- `422`: Invalid request schema.
- `500`: Server error.

---

## 📊 Data Format

- Product data is stored in `dataset_sales/data.json` as a list of product objects.
- Each product should have a `name`, `specifications` (dictionary), and `currentPrice`.
- To add new products, update `data.json` with the correct structure.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue for major changes.

---

## 📄 License

This project is licensed under the MIT License.

---
