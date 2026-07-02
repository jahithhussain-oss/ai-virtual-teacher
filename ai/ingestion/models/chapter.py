from pydantic import BaseModel

class Chapter(BaseModel):
    number: int
    title: str
    pages: list[int]