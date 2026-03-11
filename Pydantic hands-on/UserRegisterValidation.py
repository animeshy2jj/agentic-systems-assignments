from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
import re

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(min_length=6, max_length=6)

    model_config = ConfigDict(validate_assignment=True)

    
class User(BaseModel):
   user_id : int
   name : str
   email : EmailStr
   age : int = Field(ge=18)
   address : Address
   is_premium : Optional[bool] = False

   model_config = ConfigDict(validate_assignment=True)

