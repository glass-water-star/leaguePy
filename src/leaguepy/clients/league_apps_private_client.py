from .base_client import LeagueAppsBaseClient
from ..constants import LeagueAppsURLEnvs
from ..models.members import MemberResponse, MembersResponse
from ..models.transaction import TransactionsResponse
from ..models.params import league_params
from typing_extensions import Literal
from typing import Optional
from pydantic import Field


class LeagueAppsPrivateClient(LeagueAppsBaseClient):
    protocol: Literal["https"] = "https"
    version: Literal["v2"] = "v2"
    envivonment: LeagueAppsURLEnvs = LeagueAppsURLEnvs.Sandbox
    site_id: Optional[int] = None
    program_id: Optional[int] = None
    location_id: Optional[int] = None
    member_id: Optional[int] = None
    params: Optional[league_params] = Field(default=league_params())
    api_key: str
    access_token: Optional[str] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers.update({"authorization": f"Bearer {self.api_key}"})

    def get_base_url(self, env: LeagueAppsURLEnvs = LeagueAppsURLEnvs.Sandbox) -> str:
        match env:
            case LeagueAppsURLEnvs.Prod:
                return "public.leagueapps.io"
            case LeagueAppsURLEnvs.Dev:
                return "api.lapps-dev1.io"
            case LeagueAppsURLEnvs.Sandbox:
                return "api.lapps-sandbox.io"

    def get_auth_url(self, env: LeagueAppsURLEnvs = LeagueAppsURLEnvs.Sandbox) -> str:
        match env:
            case LeagueAppsURLEnvs.Prod:
                return "auth.leagueapps.io"
            case LeagueAppsURLEnvs.Dev:
                return "auth.lapps-sandbox.io"
            case LeagueAppsURLEnvs.Sandbox:
                return "auth.lapps-sandbox.io"

    def get_token(
        self,
        env: LeagueAppsURLEnvs = LeagueAppsURLEnvs.Sandbox,
        site_id: Optional[str] = None,
    ) -> str:
        match env:
            case LeagueAppsURLEnvs.Prod:
                return "auth.leagueapps.io"
            case LeagueAppsURLEnvs.Dev:
                return "auth.lapps-sandbox.io"
            case LeagueAppsURLEnvs.Sandbox:
                return "auth.lapps-sandbox.io"

    def _build_endpoint(self, endpoint: str, **kwargs) -> str:
        return f"{self.protocol}://{self.get_base_url()}/{self.version}/{endpoint}"

    def _validate_site_id(self, site_id: int = self.site_id) -> int:
        if site_id is None and self.site_id is None:
            raise ValueError("site_id must be provided")
        if self.site_id is None:
            self.site_id = site_id
        return site_id

    def _validate_program_id(self, program_id: int = self.program_id):
        if program_id is None and self.program_id is None:
            raise ValueError("site_id must be provided")
        if self.program_id is None:
            self.program_id = program_id
        return program_id

    def _validate_location_id(self, location_id: int = self.location_id):
        if location_id is None and self.location_id is None:
            raise ValueError("site_id must be provided")
        if self.location_id is None:
            self.location_id = location_id
        return location_id

    def _validate_member_id(self, member_id: int = self.member_id):
        if member_id is None and self.member_id is None:
            raise ValueError("member_id must be provided")
        if self.member_id is None:
            self.member_id = member_id
        return member_id

    def _validate_params(self, params: league_params, required: Optional[list] = None):
        if required is not None and params is None and self.params is None:
            raise ValueError(f"params must be provided. REQUIRED: {required}")
        if self.params is None:
            self.params = params
        return params

    def get_all_members(
        self, site_id: int = None, params: league_params = None
    ) -> MembersResponse:
        self._validate_site_id(site_id)
        self._validate_params(params, required=["last_updated", "last_id"])

        endpoint = f"sites/{self.site_id}/members"

        response = self.get(
            self._build_endpoint(endpoint),
            params=params.model_dump(by_alias=True, exclude_none=True),
        )
        if response.status_code == 200:
            return MembersResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_member(
        self, site_id: int = None, member_id: int = None, params: league_params = None
    ) -> MemberResponse:
        self._validate_site_id(site_id)
        self._validate_member_id(member_id)

        endpoint = f"sites/{self.site_id}/members/{self.member_id}"

        response = self.get(
            self._build_endpoint(endpoint),
            params=params.model_dump(by_alias=True, exclude_none=True),
        )
        if response.status_code == 200:
            return MemberResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_transations(
        self, site_id: int = None, params: league_params = None
    ) -> TransactionsResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/members/{self.member_id}"

        response = self.get(
            url=self._build_endpoint(endpoint),
            params=params.model_dump(by_alias=True, exclude_none=True),
        )
        if response.status_code == 200:
            return TransactionsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_product_orders(
        self, site_id: int = None, params: league_params = None
    ) -> MemberResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/export/product-orders"

        response = self.get(
            self._build_endpoint(endpoint),
            params=params.model_dump(by_alias=True, exclude_none=True),
        )
        if response.status_code == 200:
            return LeagueAppSiteResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_accounting_codes(
        self, site_id: int = self.site_id
    ) -> AccountingCodesResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/accountingCodes"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return LeagueAppSiteResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_registrations(self, site_id: int = self.site_id) -> MemberResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/export/registrations-2"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return LeagueAppSiteResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")
