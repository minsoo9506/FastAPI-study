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


u = User(name="song", birthdate="1800-06-13")

# Traceback (most recent call last):
#   File "/home/minsoo/Workspace/FastAPI-study/chap04/07_custom_validation_field.py", line 18, in <module>
#     u = User(name='song', birthdate='1800-06-13')
#   File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
# pydantic.error_wrappers.ValidationError: 1 validation error for User
# birthdate
#   Invalid Birthdate! Too old! (type=value_error)
