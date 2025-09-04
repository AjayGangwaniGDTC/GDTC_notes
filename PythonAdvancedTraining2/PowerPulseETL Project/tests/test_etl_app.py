from unittest.mock import patch
from powerpulse_etl.etl_app import PowerPulseETL

@patch("powerpulse_etl.etl_app.load_to_mysql")
@patch("powerpulse_etl.etl_app.store_to_mongo")
@patch("powerpulse_etl.etl_app.export_to_excel")
@patch("powerpulse_etl.etl_app.fetch_data", return_value=[{"mock": "data"}])
def test_etl_logging(mock_fetch, mock_excel, mock_mongo, mock_mysql, caplog):
    etl = PowerPulseETL()

    with caplog.at_level("INFO"):
        etl.run()

    assert "Starting PowerPulse ETL pipeline" in caplog.text
    assert "PowerPulse ETL pipeline completed successfully" in caplog.text
