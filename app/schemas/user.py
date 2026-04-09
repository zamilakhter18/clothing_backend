from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    email : EmailStr
    password: str
    age: int = Field(..., gt=0, description="Age must be greater than 0") 