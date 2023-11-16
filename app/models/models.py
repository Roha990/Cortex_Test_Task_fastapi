from datetime import date
from typing import Optional

from pydantic import BaseModel, constr, ValidationError, validator, field_validator, Field


class User(BaseModel):
    last_name: str = Field(min_length=3, default=None, max_length=40)
    first_name: str = Field(min_length=3, default=None, max_length=40)
    middle_name: str | None = Field(default=None)
    position_id: int
    hire_accept: date

    @field_validator('last_name', 'first_name', 'middle_name')
    @classmethod
    def validate_no_digits(cls, value):
        if any(char.isdigit() or char.isspace() or char in "!@#$%^&*()-_=+{}[]|;:'\",.<>?/" for char in value):
            raise ValueError("Недопустимые символы в имени, фамилии или отчестве")
        return value


class Position(BaseModel):
    position_name: str = Field(default=None)

    @field_validator('position_name')
    @classmethod
    def validate_no_digits(cls, value):
        if any(char.isdigit() or char.isspace() or char in "!@#$%^&*()-_=+{}[]|;:'\",.<>?/" for char in value):
            raise ValueError("Недопустимые символы в имени, фамилии или отчестве")
        return value
