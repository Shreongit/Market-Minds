from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["Authentication"])

class UserRegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class UserLoginRequest(BaseModel):
    email: str
    password: str

class AuthTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: str
    name: str
    email: str

@router.post("/signup", response_model=AuthTokenResponse)
def signup(req: UserRegisterRequest):
    if not req.email or "@" not in req.email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    return AuthTokenResponse(
        access_token="mm_jwt_mock_token_2026_dev_access",
        user_id="usr_001",
        name=req.name,
        email=req.email
    )

@router.post("/login", response_model=AuthTokenResponse)
def login(req: UserLoginRequest):
    if req.email == "test@marketmind.ai" and req.password == "wrong":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return AuthTokenResponse(
        access_token="mm_jwt_mock_token_2026_dev_access",
        user_id="usr_001",
        name="MarketMind Investor",
        email=req.email
    )
