from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List 

app = FastAPI()

users = []

class User(BaseModel):
    email: str
    is_active: bool 
    bio: Optional[str]


@app.get("/users", response_model=List[str])
async def get_users():
    return users 

@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="the ID path of the user"),
    q: str = Query(None, max_length=5)
):
    