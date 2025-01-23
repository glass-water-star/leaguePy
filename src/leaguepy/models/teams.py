from typing import Optional, List
from pydantic import BaseModel


class Team(BaseModel):
    programId: Optional[str]
    teamName: Optional[str]
    teamId: int
    division: Optional[str]
    teamStatus: Optional[str]
    teamProfileURL: Optional[str]
    dateCreated: Optional[int]
    deleted: bool
    deletedOn: Optional[int]


class TeamsResponse(BaseModel):
    __root__: List[Team]
