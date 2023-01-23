from pydantic import BaseModel, EmailStr, HttpUrl


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


user = User(email="minsoo@example.com", website="https://www.google.com")

print(user.email)
print(user.website)
