from typing import Optional, List
from pydantic import BaseModel


class Sublocation(BaseModel):
    name: str
    description: Optional[str]


class Location(BaseModel):
    locationId: int
    name: str
    description: Optional[str]
    address1: str
    address2: Optional[str]
    city: str
    state: str
    zipCode: str
    country: Optional[str]
    sublocations: List[Sublocation]


class LocationsResponse(BaseModel):
    __root__: List[Location]


class LocationResponse(BaseModel):
    __root__: Location
