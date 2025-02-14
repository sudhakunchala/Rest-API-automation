# common verification contains
# HTTP status codes
# Headers
# Data verification
# Json Schemas


def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code== expected_data, "Failed ER!=AR"

def verify_response_key(key, expected_data):
    assert key== expected_data

def verify_json_key_for_not_null_token(key):
    assert key != 0,"Failed key is not empty" + key

def verify_json_key_for_not_none(key):
    assert key is not None

def verify_json_key_for_not_null(key):
    assert key !=0,"Failed - key is non empty" + key
    assert key >0, "Failed key is greater than Zero"
def verify_response_delete(response):
    assert "Created" in response

