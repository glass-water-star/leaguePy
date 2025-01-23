from typing import Optional, List
from pydantic import BaseModel


class Program(BaseModel):
    programId: int
    deleted: bool
    masterProgramId: int
    isMaster: bool
    isSessionBased: bool
    createdOn: int
    name: str
    state: str
    visibility: str
    type: str
    code: Optional[str]
    description: Optional[str]
    summary: Optional[str]
    startTime: int
    endTime: int
    tentativeStartTime: bool
    publicRegistrationTime: Optional[int]
    endRegistrationTime: Optional[int]
    gender: str
    lastUpdated: int
    mode: str
    integrationCode: Optional[str]
    freeAgentLabel: str
    teamLabel: str
    captainLabel: str
    divisionLabel: str
    processingFeeLabel: str
    additionalTeamFeeLabel: str
    sportId: int
    sport: str
    season: str
    experienceLevel: Optional[str]
    scheduleDays: Optional[str]
    scheduleTimes: Optional[str]
    sortOrder: int
    feeRequired: bool
    regularRegistrationTime: Optional[int]
    usingVariableTeamFee: bool
    chargeMembershipFee: bool
    hasPaymentPlans: bool
    ageLimitEffectiveDate: Optional[int]
    hasWaitlist: bool
    programUrlHtml: str
    registerUrlHtml: str
    scheduleUrlHtml: str
    locationId: Optional[int]
    location: Optional[str]
    locationDescription: Optional[str]
    locationAddress1: Optional[str]
    locationAddress2: Optional[str]
    locationCity: Optional[str]
    locationState: Optional[str]
    locationZip: Optional[str]
    locationLatitude: Optional[float]
    locationLongitude: Optional[float]
    isNG: Optional[bool]
    allowTeamPlayerRegistration: Optional[bool]
    locationUrlHtml: Optional[str]


class ProgramsResponse(BaseModel):
    __root__: List[Program]
