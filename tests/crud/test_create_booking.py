import allure
import pytest

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID should'nt be null")
    @allure.description("Creating booking from the paylaod and verify that booking id shouldn't be null ")
    def test_create_booking_positive(self):
        pass