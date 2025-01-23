from pydatic import BaseModel, Field
from .constants import BackgroundCode


class public_league_params(BaseModel):
    debug_json: bool = Field(default=False, alias="debug-json")
    last_updated: int = Field(default=0, alias="last-updated")
    last_id: int = Field(default=0, alias="last-id")
    program_id: int = Field(alias="program-id")
    include_deleted: bool = Field(default=False, alias="includeDeleted")


class private_league_params(BaseModel):
    last_updated: int = Field(alias="member-id")
    last_id: int = Field(alias="last-id")


class registration_params(private_league_params):
    include_deleted: bool = Field(default=False, alias="includeDeleted")
    program_id: int = Field(alias="program-id")
    background_check_code: BackgroundCode = Field(alias="backgroundCheckCode")


class RegistrationParams(league_params):
    first_name: str = Field(alias="first-name")
    last_name: str = Field(alias="last-name")
    email: str
    phone: str
