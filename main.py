from fastapi import FastAPI, HTTPException
from specsmatch import find_similar_products
from schemas import MatchRequest
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the Product Specification Matching API!"}

@app.post("/match-products")
def match_products(request: MatchRequest):
    try:
        result = find_similar_products(request.specifications, request.top_n)
        products = result.to_dict(orient="records")
        if not products:
            raise HTTPException(status_code=404, detail="No matching products found.")
        return {"user_input": request.specifications, "matched_products": products}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

