
import fastapi 
from pydantic import BaseModel
from typing import Optional, List 

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course_api():
    return {"courses": []}

@router.get("/courses/{id}")
async def read_courses():
    return {"courses": []}

@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}

@router.delete("/courses/{id}")
async def delete_courses():
    return {"courses": []}
