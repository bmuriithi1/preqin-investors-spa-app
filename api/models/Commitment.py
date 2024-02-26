from pydantic import BaseModel, PositiveInt


class Commitment(BaseModel):
    id: PositiveInt
    asset_class: str
    firm_id: PositiveInt
    currency: str
    amount: str
