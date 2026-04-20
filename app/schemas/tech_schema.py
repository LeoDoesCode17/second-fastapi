from pydantic import BaseModel
class TechResponse(BaseModel):
    id: int
    name: str
    slug: str

class TechCreate(BaseModel):
    name: str
    slug: str

class TechUpdate(TechCreate):
    pass
