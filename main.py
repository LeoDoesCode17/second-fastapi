from fastapi import FastAPI
from app.exceptions.tech_exceptions import DuplicateTechSlugException
from app.exceptions.hanlders import duplicate_tech_slug_handler
from app.api.endpoints import tech, auth, image

app = FastAPI()
app.add_exception_handler(DuplicateTechSlugException, duplicate_tech_slug_handler)
app.include_router(auth.router)
app.include_router(tech.router)
app.include_router(image.router)
