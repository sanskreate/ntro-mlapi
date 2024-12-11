from pydantic import BaseModel
from typing import Dict

class MatchRequest(BaseModel):
    specifications: Dict[str, str]
    top_n: int = 5
