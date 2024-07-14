from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List 
from api import courses, sections, users



app = FastAPI()

app.include_router(courses.router)
app.include_router(users.router)
app.include_router(sections.router)