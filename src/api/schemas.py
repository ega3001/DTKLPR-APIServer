from typing import List
from pydantic import BaseModel


class RecognizedPlatesList(BaseModel):
    count: int
    plates: List[str]