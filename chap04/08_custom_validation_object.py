from pydantic import BaseModel, ValidationError, root_validator


class User(BaseModel):
    id: str
    password: str
    password_confirm: str

    @root_validator
    def check_password(cls, values):  # values는 object
        password = values.get("password")
        password_confirm = values.get("password_confirm")
        if password != password_confirm:
            return ValidationError("Password doesn't match!")
        return values
