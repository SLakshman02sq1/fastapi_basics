from pydantic import BaseModel,ConfigDict,EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr

class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr

    model_config = ConfigDict(from_attributes=True) # to enable reading data from non-dictionary sources, specifically object attributes