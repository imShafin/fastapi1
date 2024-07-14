import fastapi 
from pydantic import BaseModel
from typing import Optional, List 

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool 
    bio: Optional[str]


@router.get("/users", response_model=List[str])
async def get_users():
    return users 

@router.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{id}")
async def get_user(
    id: int,
    q: str 
):
    pass  
