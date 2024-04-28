from pydantic import BaseModel, Field, EmailStr
from typing import Union

from typing import Union
from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    Seed_RepDate: int = Field(default=None)
    Seed_Year: int = Field(default=None)
    Seeds_YearWeek: int = Field(default=None)
    Seed_Varity: str = Field(default=None)
    Seed_RDCSD: str = Field(default=None)
    Seed_Stock2Sale: int = Field(default=None)
    Seed_Season: int = Field(default=None)
    Seed_Crop_Year: Union[str, int] = Field(default=None)
    
    class Config:
        schema_extra = {
            "post demo": { 
                "Seed_RepDate": " Seed_RepDate ",
                "Seed_Year": " Seed_Year ",
                "Seeds_YearWeek": " Seeds_YearWeek ",
                "Seed_Varity": " Seed_Varity ",
                "Seed_RDCSD": " Seed_RDCSD ",
                "Seed_Stock2Sale": " Seed_Stock2Sale ",
                "Seed_Season": " Seed_Season ",
                "Seed_Crop_Year": " Seed_Crop_Year "
            }
        }

        
class UpdateSchema(BaseModel):
    Seed_RepDate: int = Field(default=None)
    Seed_Year: int = Field(default=None)
    Seeds_YearWeek: int = Field(default=None)
    Seed_Varity: str = Field(default=None)
    Seed_RDCSD: str = Field(default=None)
    Seed_Stock2Sale: int  = Field(default=None)
    Seed_Season: int = Field(default=None)
    Seed_Crop_Year: Union[int, str] = Field(default=None)

    class Config:
        schema_extra = {
            "Update demo": {
                "type": "object",
                "properties": {
                    "Seed_RepDate": {"type": ["string", "integer"]},
                    "Seed_Year": {"type": ["string", "integer"]},
                    "Seeds_YearWeek": {"type": ["string", "integer"]},
                    "Seed_Varity": {"type": "string"},
                    "Seed_RDCSD": {"type": "string"},
                    "Seed_Stock2Sale": {"type": ["string", "integer"]},
                    "Seed_Season": {"type": ["string", "integer"]},
                    "Seed_Crop_Year": {"type": ["string", "integer"]}
                }
            }
        }
          
class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    Email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "fullname": "klui",
                "Email": "please@helpme.com",
                "password": "ineedhelp"
            }
        }
        
class LoginSchema(BaseModel):
    Email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    
    class Config:
        the_schema = {
            "user_demo":{
                "email": "helpme@gmail.com",
                "password": "1234"
            }
        }