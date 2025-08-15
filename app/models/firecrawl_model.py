from typing import Dict, Any, List

from pydantic import BaseModel

class ResultFirecrawl(BaseModel):
    data: Dict[str, Any] | List
