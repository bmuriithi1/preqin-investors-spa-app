import os

import pytest
from api.main import app
from api.models.CommitmentData import CommitmentData
from api.models.InvestorData import InvestorData
from fastapi import status
from fastapi.testclient import TestClient

client: TestClient = TestClient(app)
PREQIN_API_ENDPOINT = os.getenv("PREQIN_API_ENDPOINT")
API_PREFIX: str = "/investor-data"


class TestGetInvestmentDataAPI:

    @pytest.fixture
    def investor_data(self):
        investor_data = [
            {
                "firm_id": 2670,
                "firm_name": "Mjd Jedi fund",
                "firm_type": "bank",
                "date_added": "2010-06-08T00:00:00Z",
                "address": "29 Nathan Road, Hong Kong",
            },
        ]

        return investor_data

    # TODO: Mock out Preqin API request. This is currently an integration test, not a unit test.
    def test_get_investor_data(self, investor_data):
        investor_ids = "2670"
        response = client.get(
            f"{API_PREFIX}/get-investor-data?investor_ids={investor_ids}"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == investor_data


class TestGetCommitmentData:

    @pytest.fixture
    def commitment_data(self):
        commitment_data = [
            {"asset_class": "hf", "currency": "EUR", "amount": "51M"},
            {"asset_class": "hf", "currency": "USD", "amount": "15M"},
            {"asset_class": "hf", "currency": "SGD", "amount": "62M"},
            {"asset_class": "hf", "currency": "EUR", "amount": "78M"},
            {"asset_class": "hf", "currency": "HKD", "amount": "39M"},
            {"asset_class": "hf", "currency": "SGD", "amount": "41M"},
            {"asset_class": "hf", "currency": "GBP", "amount": "43M"},
            {"asset_class": "hf", "currency": "SGD", "amount": "56M"},
            {"asset_class": "hf", "currency": "EUR", "amount": "38M"},
            {"asset_class": "hf", "currency": "HKD", "amount": "88M"},
            {"asset_class": "hf", "currency": "SGD", "amount": "37M"},
        ]

        return commitment_data

    # TODO: Mock out Preqin API request. This is currently an integration test, not a unit test.
    def test_get_commitment_data(self, commitment_data):
        asset_class = "hf"
        investor_id = "2792"

        URL = f"{API_PREFIX}/get-investor-commitment-info?asset_class={asset_class}&investor_id={investor_id}"
        response = client.get(URL)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == commitment_data
