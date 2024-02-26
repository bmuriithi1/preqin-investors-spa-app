import json
import os
from typing import Any, Generator, List

import requests
from api.models.Commitment import Commitment
from api.models.CommitmentData import CommitmentData
from api.models.Firm import Firm
from api.models.InvestorData import InvestorData
from fastapi import APIRouter, HTTPException, status

PREQIN_API_ENDPOINT = os.getenv("PREQIN_API_ENDPOINT")
INVESTOR_KEYS = ["firm_id", "firm_name", "firm_type", "date_added", "address"]
COMMITMENT_KEYS = ["asset_class", "amount", "currency"]
ASSET_CLASSES = ["pe", "pd", "re", "inf", "nr", "hf"]
INVESTOR_IDS = [2670, 2792, 332, 3611]

router: APIRouter = APIRouter(prefix="/investor-data")


# TODO: Mock/patch this method out in tests to supply responses for testing
def make_url_request(url: str) -> List[dict[str, Any]]:
    response = requests.get(url=url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error whilst accessing Preqin APIs",
        )
    data = response.json()

    return data


# TODO: Add test for this method using a pytest fixture for the response data
def process_investor_data(
    investor_ids: str, response_data: List[dict[str, Any]]
) ->  List[dict[str, Any]]:

    investor_list: List[int] = [int(str) for str in investor_ids.split(",")]
    firm_generator: Generator[dict[str, Any], None, None] = (
        firm for firm in response_data if firm["firm_id"] in investor_list
    )

    investor_data: List[dict[str, Any]] = []
    for firm in firm_generator:
        investor_info: dict[str, Any] = {key: firm[key] for key in INVESTOR_KEYS if key in firm}
        investor_data.append(investor_info)

    return investor_data


# TODO: Add tests for this in pytest harness, using a pytest fixture for the response data
def process_commitment_data(
    response_data: List[dict[str, Any]]
) -> List[dict[str, Any]]:

    commitment_data: List[dict[str, Any]] = []
    for commitment in response_data:
        commitment_info = {
            key: commitment[key] for key in COMMITMENT_KEYS if key in commitment
        }
        commitment_data.append(commitment_info)

    return commitment_data


@router.get("/get-investor-data", response_model=List[InvestorData])
def get_investor_data(investor_ids: str) -> List[dict[str, Any]]:
    """
    Fetches and returns investor data for given investor IDs
    """

    # Get data from Preqin endpoint
    URL = f"{PREQIN_API_ENDPOINT}/api/investors"
    data = make_url_request(URL)

    # Process response to obtain relevnat firm info
    investor_data: List[dict[str, Any]] = process_investor_data(investor_ids, data)

    # Raise exception (HTTP 404 Not found) if no investor data was found
    if len(investor_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Investors not found"
        )

    return investor_data


@router.get("/get-investor-commitment-info", response_model=List[CommitmentData])
def get_commitment_data(asset_class: str, investor_id: int) -> List[dict[str, Any]]:
    """
    Fetches and returns commitment data for given investor ID and asset class
    """

    # Parse inputs
    if asset_class not in ASSET_CLASSES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Asset class {asset_class} doesn't exist",
        )

    # Get data from Preqin endpoint
    URL = f"{PREQIN_API_ENDPOINT}/api/investor/commitment/{asset_class}/{investor_id}"
    data = make_url_request(URL)

    # Process response
    commitment_data: List[dict[str, Any]] = process_commitment_data(data)

    # Raise exception (HTTP 404 Not found) if no commitment data was found
    if len(commitment_data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Commitment data not found"
        )

    return commitment_data
