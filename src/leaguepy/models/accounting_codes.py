from typing import List
from pydantic import BaseModel


class AccountingCode(BaseModel):
    label: str
    values: List[str]


class AccountingCodesResponse(BaseModel):
    acccountingCode1: AccountingCode
    acccountingCode2: AccountingCode
