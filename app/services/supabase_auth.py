# app/services/supabase_auth.py
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends, status
from app.services.supabase_client import supabase
from app.exceptions.auth_exception import AuthFailException

bearer_scheme = HTTPBearer()

# Dependency to get current user:
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):    
    """
    Validates the Bearer JWT sent by the client.
    Supabase signs tokens with HS256 using your project's JWT secret.
    """
    # when executing protected API, get: detail: not authenticated
    print(f'credentials: {credentials}')
    token = credentials.credentials 
    print(f'token is {token}')
    try:
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bad request: {e}"
        )
    
def login(user_login_data: dict):
    response = supabase.auth.sign_in_with_password({
        "email": user_login_data["email"],
        "password": user_login_data["password"]
    })
    if not response.session:
        raise AuthFailException("Incorrect credentials")
    return response
        
def logout():
    supabase.auth.sign_out()
