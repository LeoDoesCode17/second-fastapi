# app/api/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.services import supabase_auth
from app.schemas.auth_schema import UserLogin

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post("/login")
async def login(user_login: UserLogin):
    try:
        response = supabase_auth.login(user_login_data=user_login.model_dump())
        return {
            "access_token": response.session.access_token, #access token from login session, must be saved
            "token_type": "bearer",
            "user_id": response.user.id,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'{e}',
        )
    
@router.post("/logout")
async def logout(current_user=Depends(supabase_auth.get_current_user)):
    supabase_auth.logout()
    return {"event": "logout", "status": "ok"}


 