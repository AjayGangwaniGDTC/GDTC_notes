from powerpulse_etl.mysql_loader import load_to_mysql
from unittest.mock import patch

@patch("powerpulse_etl.mysql_loader.mysql.connector.connect")
def test_inserting_to_msql(mock_connect):
    mock_conn = mock_connect.return_value
    mock_cursor = mock_conn.cursor.return_value
    
    test_data = [{
        "stateId": "MH",
        "period": "2000",
        "producerTypeDescription": "All sectors",
        "energySourceDescription": "Petroleum",
        "generation": 999.9
    }]
    
    load_to_mysql(test_data)
    
    assert mock_cursor.execute.called
    assert mock_conn.commit.called