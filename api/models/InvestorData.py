from datetime import datetime
from pydantic import BaseModel, PositiveInt


class InvestorData(BaseModel):
    firm_id: PositiveInt
    firm_name: str
    firm_type: str
    date_added: datetime
    address: str
