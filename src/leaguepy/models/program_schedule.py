from typing import Optional, List
from pydantic import BaseModel


class Game(BaseModel):
    scheduleItemType: str
    gameId: Optional[int]
    type: str
    typeLabel: Optional[str]
    state: str
    stateLabel: Optional[str]
    startTime: int
    team1Id: Optional[int]
    team1: Optional[str]
    team1Seed: Optional[int]
    team1Score: Optional[int]
    team1Result: Optional[int]
    team2: Optional[str]
    team2Seed: Optional[int]
    team2Score: Optional[int]
    team2Result: Optional[int]
    locationId: Optional[int]
    locationName: Optional[str]
    subLocationId: Optional[int]
    subLocationName: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    round: Optional[int]
    notes: Optional[str]
    eventId: Optional[int]
    teamId: Optional[int]
    teamName: Optional[str]
    title: Optional[str]
    startDate: Optional[int]
    endDate: Optional[int]
    description: Optional[str]
    location: Optional[str]
    locationLabel: Optional[str]
    allowEdit: Optional[bool]


class Note(BaseModel):
    noteId: int
    startTime: int
    color: str
    message: str


class ScheduleResponse(BaseModel):
    games: List[Game]
    notes: List[Note]
