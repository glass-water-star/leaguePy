from typing import Optional, List
from pydantic import BaseModel, TypeAdapter


class Transaction(BaseModel):
    siteId: int
    id: int
    transactionItemId: int
    lastUpdated: int
    type: str
    gateway: str
    amount: float
    netAmount: float
    netTotalAmount: float
    userId: int
    firstName: str
    lastName: str
    programId: int
    programName: str
    programType: str
    programCode: Optional[str]
    accountingCode1: str
    accountingCode2: str
    masterProgramId: Optional[int]
    masterProgramName: Optional[str]
    masterProgramType: Optional[str]
    masterProgramCode: Optional[str]
    productOrderId: Optional[int]
    productId: Optional[int]
    productName: Optional[str]
    teamId: Optional[int]
    teamName: Optional[str]
    bankTransferId: Optional[str]
    bankTransferDate: Optional[int]
    created_on: int
    programStartDate: int
    programEndDate: int
    invoiceId: int
    registrationId: Optional[int]
    containerInvoiceId: Optional[int]

Registrations = TypeAdapter(List[Transaction])
