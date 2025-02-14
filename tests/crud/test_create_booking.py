import allure
import pytest

from src.helpers.api_request_wrapper import *
from src.constants.api_constant import *
from src.helpers.payload_manager import *
from src.helpers.common_verifications import *
from src.utils.utils import Utils
import logging



class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID should'nt be null")
    @allure.description("Creating booking from the paylaod and verify that booking id shouldn't be null ")
    def test_create_booking_positive(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth= None,
            headers=Utils().common_headers_jsons(),
            payload=payload_create_booking(),
            in_json= False
        )
        verify_http_status_code(response_data=response, expected_data=200)
        verify_json_key_for_not_null_token(response.json()["bookingid"])
