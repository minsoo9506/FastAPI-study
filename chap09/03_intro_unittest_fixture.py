from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: address


import pytest


@pytest.fixture
def address():
    return Address(
        street_address="12 Squirell Street",
        postal_code="424242",
        city="Woodtown",
        country="US",
    )


@pytest.fixture
def person(address):
    return Person(
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address=address,
    )


def test_address_country(address):
    assert address.country == "US"


def test_person_first_name(person):
    assert person.first_name == "John"


def test_person_address_city(person):
    assert person.address.city == "Woodtown"
