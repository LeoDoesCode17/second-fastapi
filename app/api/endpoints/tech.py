# app/api/endpoints/tech.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.services import tech_service
from app.schemas.tech_schema import TechCreate, TechResponse, TechUpdate
from app.exceptions.tech_exceptions import UpdateTechFailException
from app.services.supabase_auth import get_current_user
import ast

router = APIRouter(
    prefix='/techs',
    tags=['Techs']
)

@router.get("/extract-error")
async def extract_error():
    # Your specific string (Python-style formatting)
    raw_string = "{'message': 'duplicate key value violates unique constraint \"techs_slug_key\"', 'code': '23505', 'hint': None, 'details': None}"
    
    try:
        # Use ast.literal_eval because the string uses single quotes and 'None'
        data_dict = ast.literal_eval(raw_string)
        
        # Extract the 'message' key
        error_message = data_dict.get("message", "No message found")
        
        return {"extracted_message": error_message}
        
    except (ValueError, SyntaxError) as e:
        raise HTTPException(status_code=400, detail=f"Failed to decode string: {str(e)}")
    
@router.post("/", response_model=TechResponse)
async def create_new_tech(
    tech: TechCreate,
    current_user=Depends(get_current_user)
):
    try:
        created_tech = tech_service.create_tech(data=tech.model_dump())
        return created_tech
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )
    
@router.get("/", response_model=list[TechResponse])
async def get_all_techs():
    try:
        techs = tech_service.get_all_techs()
        return techs
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )

@router.patch("/{id}", response_model=TechResponse)
async def update_tech(
    id: int,
    tech_data: TechUpdate,
    current_user = Depends(get_current_user)
):
    try:
        updated_tech = tech_service.update_tech(id=id, data=tech_data.model_dump())
        return updated_tech
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{e}'
        )
