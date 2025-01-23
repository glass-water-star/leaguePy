from enum import Enum


class LeagueAppsURLEnvs(Enum):
    """
    Enum representing the different environments for LeagueApps URLs.
    https://leagueapps.notion.site/Public-API-overview-450d53df689c47cb89593d453c73a6c9

    Attributes:
        Prod (str): Represents the Production environment.
        Dev (str): Represents the Development environment.
        Sandbox (str): Represents the Sandbox environment.

    These environments are used to differentiate between the various stages of deployment and testing
    for the LeagueApps API. Each environment corresponds to a specific set of URLs and configurations
    as outlined in the LeagueApps Public API overview.
    """

    Prod = "Production"
    Dev = "Dev1"
    Sandbox = "Sandbox"


class APIType(Enum):
    Public = "Public"
    Private = "Private"


class PayStatus(Enum):
    OPEN_PAID = "Open_Paid"
    OPEN_NEW = "Open_New"
    CANCELLED = "Cancelled"
    CLOSED = "Closed"


class BackgroundCode(Enum):
    YS = "YS"  # Yardstick
    AN = "AN"  # Ankored


class RegistrationStatus(Enum):
    SPOT_RESERVED = "SPOT_RESERVED"
    SPOT_PENDING = "SPOT_PENDING"
    REMOVED = "REMOVED"
    WAITING_LIST = "WAITING_LIST"


class UserType(Enum):
    ADULT = "ADULT"
    CHILD = "CHILD"
    ORPHAN = "ORPHAN"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class PaymentStatus(Enum):
    NA_FREE = "NA_FREE"
    NA_TEAM_PAYS = "NA_TEAM_PAYS"
    NA_WAITLIST = "NA_WAITLIST"
    PAID = "PAID"
    PARTIAL = "PARTIAL"
    REFUND = "REFUND"
    UNPAID = "UNPAID"
    VOID = "VOID"


class ProgramType(Enum):
    LEAGUE = "LEAGUE"
    EVENT = "EVENT"
    TOURNAMENT = "TOURNAMENT"
    CAMP = "CAMP"
    CLUBTEAM = "CLUBTEAM"
    CLASS = "CLASS"


class Role(Enum): # Can't use role as the sample response is inconsistent
    FREEAGENT = "FREEAGENT"
    PLAYER = "PLAYER"
    CAPTAIN = "CAPTAIN"


class ProgramState(Enum):
    COMPLETED = "COMPLETED"
    DRAFT = "DRAFT"
    LIVE = "LIVE"
    UPCOMING = "UPCOMING"

class OrgRole(Enum):
    ORG_ACC_OWNER = "ORG_ACC_OWNER"
    SITE_ADMIN = "SITE_ADMIN"
    ORG_ACC_ADMIN = "ORG_ACC_ADMIN"
    UNAUTHORIZED = "UNAUTHORIZED"
    SITE_REPORTER = "SITE_REPORTER"
    SITE_MANAGER = "SITE_MANAGER"
    PROGRAM_ADMIN = "PROGRAM_ADMIN"
    SITE_COORDINATOR = "SITE_COORDINATOR"
    SITE_DIRECTOR = "SITE_DIRECTOR"
