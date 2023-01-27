from datetime import datetime, timedelta

from authentication.password import generate_token
from pydantic import BaseModel, EmailStr, Field
from tortoise import fields, timezone
from tortoise.models import Model


# token의 verify한 기간 지정
def get_expiration_date(duration_seconds: int = 86400) -> datetime:
    return timezone.now() + timedelta(seconds=duration_seconds)


class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class UserDB(User):
    hashed_password: str


class AccessToken(BaseModel):
    user_id: int
    access_token: str = Field(default_factory=generate_token)
    expiration_date: datetime = Field(default_factory=get_expiration_date)

    class Config:
        orm_mode = True


class UserTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    email = fields.CharField(index=True, unique=True, null=False, max_length=255)
    hashed_password = fields.CharField(null=False, max_length=255)

    class Meta:
        table = "users"


class AccessTokenTortoise(Model):
    access_token = fields.CharField(pk=True, max_length=255)
    user = fields.ForeignKeyField("models.UserTortoise", null=False)
    expiration_date = fields.DatetimeField(null=False)

    class Meta:
        table = "access_tokens"
