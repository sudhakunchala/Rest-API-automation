import allure
import pytest
import logging

from src.helpers.api_request_wrapper import *
from src.constants.api_constant import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import Utils

class TestCRUDBooking(object):
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        verify_response_key(response.json()["firstname"], "Amit")
        verify_response_key(response.json()["lastname"], "Brown")
        verify_http_status_code(response_data=response, expected_data=200)

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expected_data=201)