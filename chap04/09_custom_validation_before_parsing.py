from typing import List

from pydantic import BaseModel, ValidationError, validator


class User(BaseModel):
    id: str
    password: List[int]

    @validator("password", pre=True)
    def split_str_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


u = User(id="minsoo", password="1,2,3")
print(u)
# id='minsoo' password=[1, 2, 3]
