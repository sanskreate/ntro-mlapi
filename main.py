from fastapi import FastAPI, Depends, status, Response, HTTPException
from specsmatch import find_similar_products
import uvicorn
from schemas import MatchRequest


app = FastAPI()


@app.post("/match-products")
def match_products(request: MatchRequest):
    try:
        result = find_similar_products(request.user_input, request.top_n)
        products = result.to_dict(orient="records")
        return {"user_input": request.user_input, "matched_products": products}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Specification Matching API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)