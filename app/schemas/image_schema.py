from pydantic import BaseModel

class ImageResponse(BaseModel):
    name: str
    alt_text: str
    url: str

class ImageCreate(BaseModel):
    name: str
    url: str
    alt_text: str

class ImageUpdate(BaseModel):
    name: str | None = None
    url: str | None = None
    alt_text: str | None = None