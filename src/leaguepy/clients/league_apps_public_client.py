from typing import Optional
from .base_client import LeagueAppsBaseClient
from ..constants import LeagueAppsURLEnvs
from ..models.program_info import LeagueAppSiteResponse
from typing_extensions import Literal


class LeagueAppsPublicClient(LeagueAppsBaseClient):
    protocol: Literal["https"] = "https"
    version: Literal["v1"] = "v1"

    program_id: Optional[int] = None
    location_id: Optional[int] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers.update({"la-api-key": self.api_key})

    def get_base_url(self, env: LeagueAppsURLEnvs = LeagueAppsURLEnvs.Sandbox) -> str:
        match env:
            case LeagueAppsURLEnvs.Prod:
                return "public.leagueapps.io"
            case LeagueAppsURLEnvs.Dev:
                return "admin.lapps-dev1.io"
            case LeagueAppsURLEnvs.Sandbox:
                return "admin.lapps-sandbox.io"

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

    def get_site_info(self, site_id: int = self.site_id):
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return LeagueAppSiteResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_current_programs(self, site_id: int = self.site_id) -> ProgramsResponse:
        self._validate_site_id(site_id)
        self._validate_program_id(program_id)

        endpoint = f"sites/{site_id}/programs/current"

        response = self.get(self._build_endpoint(endpoint))

        if response.status_code == 200:
            return ProgramsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_program(
        self, site_id: int = self.site_id, program_id: int = self.program_id
    ) -> ProgramsResponse:
        self._validate_site_id(site_id)
        self._validate_program_id(program_id)

        endpoint = f"sites/{self.site_id}/programs/{self.program_id}"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return ProgramsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_program_schedule(
        self, site_id: int = self.site_id, program_id: int = self.program_id
    ) -> ScheduleResponse:
        self._validate_site_id(site_id)
        self._validate_program_id(program_id)

        endpoint = f"sites/{self.site_id}/programs/{self.program_id}/schedule"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return ScheduleResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_program_teams(
        self,
        site_id: int = self.site_id,
        program_id: int = self.program_id,
        includeDeleted: bool = False,
    ) -> TeamsResponse:
        self._validate_site_id(site_id)
        self._validate_program_id(program_id)

        endpoint = f"sites/{self.site_id}/programs/{self.program_id}/teams"

        response = self.get(
            self._build_endpoint(endpoint), params={"includeDeleted": includeDeleted}
        )
        if response.status_code == 200:
            return ScheduleResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_all_locations(self, site_id: int = self.site_id) -> LocationsResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/programs/locations"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return ProgramsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_location(
        self, site_id: int = self.site_id, location_id: int = self.location_id
    ) -> LocationResponse:
        self._validate_site_id(site_id)
        self._validate_location_id(location_id)

        endpoint = f"sites/{self.site_id}/programs/locations/{self.location_id}"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return ProgramsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_blogs(self, site_id: int = self.site_id) -> BlogsResponse:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/blog"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return ProgramsResponse(**response.json())
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_sports(self, site_id: int = self.site_id) -> dict:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/sports"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get site info: {response.text}")

    def get_announcements(self, site_id: int = self.site_id) -> dict:
        self._validate_site_id(site_id)

        endpoint = f"sites/{self.site_id}/announcements"

        response = self.get(self._build_endpoint(endpoint))
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get site info: {response.text}")
