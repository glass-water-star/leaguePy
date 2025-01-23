from typing import Optional, List
from pydantic import BaseModel, Field, TypeAdapter
from ..constants import (
    Role,
    ProgramState,
    RegistrationStatus,
    UserType,
    Gender,
    PaymentStatus,
    ProgramType,
)


class Registration(BaseModel):
    registrationId: int
    registrationStatus: Optional[RegistrationStatus] = None
    siteName: Optional[str]= None
    lastUpdated: Optional[int]= None
    id: Optional[int]= None
    created: Optional[int]= None
    userId: Optional[int]= None
    userName: Optional[str]= None
    firstName: Optional[str]= None
    lastName: Optional[str]= None
    userType: Optional[UserType] = Field(UserType.ADULT)
    userProfileId: Optional[int]= None
    photo: Optional[str]= None
    birthDate: Optional[int]= None
    gender: Optional[Gender]= None
    phone: Optional[str]= None
    address1: Optional[str]= None
    address2: Optional[str]= None
    city: Optional[str]= None
    state: Optional[str]= None
    zipCode: Optional[str]= None
    groupName: Optional[str]= None
    groupId: Optional[int]= None
    parentUserId: Optional[int]= None
    parentFirstName: Optional[str]= None
    parentLastName: Optional[str]= None
    parentEmail: Optional[str]= None
    parentPhone: Optional[str]= None
    email: Optional[str]= None
    paymentStatus: Optional[PaymentStatus]= None
    invoiceId: Optional[int]= None
    totalAmountDue: Optional[float]= None
    outstandingBalance: Optional[float]= None
    lastPaymentDate: Optional[int]= None
    amountPaid: Optional[float]= None
    price: Optional[float]= None
    discountCode: Optional[str]= None
    paymentPlan: Optional[str]= None
    paymentPlanStatus: Optional[ProgramState] = Field(default_factory=lambda x: None if x == "NULL" else x)
    programId: Optional[int]= None
    masterProgramId: Optional[int]= None
    masterProgramName: Optional[str]= None
    programCode: Optional[str]= None
    integrationCode: Optional[str]= None
    programType: Optional[ProgramType]= None
    programName: Optional[str]= None
    host: Optional[str]= None
    programState: Optional[ProgramState]= None
    programStartDate: Optional[int]= None
    programEndDate: Optional[int]= None
    registrationStartDate: Optional[int]= None
    registrationEndDate: Optional[int]= None
    sportId: Optional[int]= None
    sport: Optional[str]= None
    role: Optional[str]= None# Can't use role as the sample response is inconsistent
    isStaff: Optional[bool]= None
    teamId: Optional[int]= None
    team: Optional[str]= None
    division: Optional[str]= None
    season: Optional[str] = None
    location: Optional[str]= None
    locationId: Optional[int]= None
    waiverAcceptedTimestamp: Optional[int]= None
    notes: Optional[str]= None
    deletedOn: Optional[int]= None
    deleted: Optional[bool]= None
    WhatGradeAreYouIn: Optional[str]= None
    TShirtSize: Optional[str]= None
    CurrentGrade: Optional[str]= None
    backgroundCheckLastUpdated: Optional[str]= None
    backgroundCheckStatus: Optional[str]= None

Registrations = TypeAdapter(List[Registration])


