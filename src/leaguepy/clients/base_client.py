import pydantic
import jwt
from requests import Session
import time
import abc
from typing import Literal


class LeagueAppsBaseClient(Session, BaseModel):
    site_id: int
    api_key: str
    protocol: str = "https"  # The only protocol that LeagueApps uses is HTTPS
    version: Literal["v1", "v2"] = (
        "v1"  # v1 seems to be the public API version and v2 seems to be the private API version
    )

    def __init__(self, *args, **kwargs):
        super().__(*args, **kwargs)

    def get_base_url(env: LeagueAppsURLEnvs, api_type: APIType) -> str:
        match api_type:
            case APIType.Public:
                return get_public_base_url(env)
            case APIType.Private:
                return get_private_base_url(env)

    def get_endpoint(self, endpoint: str):
        return f"{self.get_base_url()}/{self.version}/{endpoint}"
