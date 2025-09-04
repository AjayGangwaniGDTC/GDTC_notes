import os
import pandas as pd
from powerpulse_etl.excel_exporter import export_to_excel
from powerpulse_etl.config import EXCEL_PATH

def test_export_to_excel_creates_file():
    test_data = [{"stateId": "TX", "period": "2023"}]
    export_to_excel(test_data)
    assert os.path.exists(EXCEL_PATH)
    
    df = pd.read_excel(EXCEL_PATH)
    assert "stateId" in df.columns
