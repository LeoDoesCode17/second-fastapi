# app/api/endpoints/image.py
from app.services.supabase_auth import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.exceptions import ResponseValidationError
from app.services import image_service
from app.schemas.image_schema import ImageResponse, ImageCreate, ImageUpdate

router = APIRouter(
    prefix='/images',
    tags=['Images']
)

@router.get("/", response_model=list[ImageResponse])
async def read_all_images():
    try:
        images = image_service.get_all_images()
        return images
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )
    
@router.post("/", response_model=ImageResponse)
async def create_new_image(image: ImageCreate, current_user = Depends(get_current_user)):
    try:
        created_image = image_service.create_image(data=image.model_dump())
        return created_image
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )

@router.patch("/{id}", response_model=ImageResponse)
async def update_image(id: int, image: ImageUpdate, current_user = Depends(get_current_user)):
    try:
        updated_image = image_service.update_image(id=id, data=image.model_dump())
        return updated_image
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )