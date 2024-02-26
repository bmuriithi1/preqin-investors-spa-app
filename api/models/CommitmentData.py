from pydantic import BaseModel


class CommitmentData(BaseModel):
    asset_class: str
    currency: str
    amount: str
