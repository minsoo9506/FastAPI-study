from datetime import date

from pydantic import BaseModel, validator


class User(BaseModel):
    name: str
    birthdate: date

    @validator("birthdate")  # argument로 birthdate
    def valid_birthdate(cls, v: date):  # classmethod
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("Invalid Birthdate! Too old!")
        return v
