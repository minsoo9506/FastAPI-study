from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    male = "M"
    female = "F"


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender  # Enum class를 (상속하여 원하는 class 만들고) gender field로 이용
    birthdate: date
    age: int
    interest: List[str]


if __name__ == "__main__":
    try:
        p1 = Person(
            first_name="minsoo",
            last_name="song",
            gender="M",
            birthdate="1995-06-13",
            age=29,
            interest=["soccer", "youtube"],
        )
        print(p1)
    except ValidationError as e:
        print(e)

# first_name='minsoo' last_name='song' gender=<Gender.male: 'M'> birthdate=datetime.date(1995, 6, 13) age=29 interest=['soccer', 'youtube']
