import datetime
from typing import Optional, List
from leaguepy.constants import Gender, OrgRole, UserType
from pydantic import BaseModel, TypeAdapter


class Member(BaseModel):
    userId: Optional[int] = None 
    id: Optional[int] = None
    firstName: str
    lastName: Optional[str] = None
    email: Optional[str]
    type: Optional[UserType] = None
    username: Optional[str] = None
    orgAccountRole: Optional[OrgRole] = None
    lastLogin: Optional[datetime.datetime] = None
    deleted: bool
    deletedOn: Optional[int]
    lastUpdated: Optional[datetime.datetime] = None
    newsletterOptIn: bool
    dateJoined: Optional[datetime.datetime]
    userProfileId: int
    photo: Optional[str] = None
    gender: Optional[Gender] = None
    birthDate: Optional[datetime.datetime] = None
    mobilePhone: Optional[str] = None
    groupName: Optional[str] = None
    groupId: Optional[int] = None
    membershipName: Optional[str] = None
    membershipExpiration: Optional[datetime.datetime] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    country: Optional[str] = None
    shipAddress1: Optional[str]= None
    shipAddress2: Optional[str]= None
    shipCity: Optional[str]= None
    shipState: Optional[str]= None
    shipZipCode: Optional[str]= None
    shipCountry: Optional[str]= None


Members = TypeAdapter(List[Member])
