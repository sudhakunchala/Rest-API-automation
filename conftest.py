import allure
import pytest
import openpyxl

from src.helpers.api_request_wrapper import post_request
from src.constants.api_constant import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import Utils

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_jsons(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            auth=None,
                            headers=Utils().common_headers_jsons(),
                            payload=payload_create_booking(),
                            in_json=False)

    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants().url_create_booking(),
                            auth=None,
                            headers=Utils().common_headers_jsons(),
                            payload=payload_create_booking(),
                            in_json=False)

    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id