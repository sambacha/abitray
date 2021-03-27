from typing import Optional

from pydantic import BaseModel, Field


class BaseField(BaseModel):
    password: Optional[str]


class AddABI(BaseField):
    text: str = Field(...)


class GetABI(BaseField):
    id: str = Field(...)
