from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    nickname: str
    location: Optional[str]
    age: int = 0


user = User(nickname="mason")

print(user)
# nickname='mason' location=None age=0
