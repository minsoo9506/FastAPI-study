from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)
