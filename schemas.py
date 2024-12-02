from pydantic import BaseModel

class MatchRequest(BaseModel):
    user_input: str
    top_n: int = 5  