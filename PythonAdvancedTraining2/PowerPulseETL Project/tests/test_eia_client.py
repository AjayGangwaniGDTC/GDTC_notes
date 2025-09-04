from unittest.mock import patch
from powerpulse_etl.eia_client import fetch_data

@patch("powerpulse_etl.eia_client.requests.get")
def test_fetch_data_returns_valid_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "response": {"data": [{"stateId": "CA", "period": "2023"}]}
    }

    data = fetch_data()
    assert isinstance(data, list)
    assert data[0]["stateId"] == "CA"
