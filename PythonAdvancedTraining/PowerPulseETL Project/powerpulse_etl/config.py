'''This file is the configuration file. All the necessary data required for it 
project is stored here in the form of variables so that only variables can be 
called and code can be reused'''

import os
import logging

# Environment Configuration so that only variable name can be called directly
EIA_API_KEY = os.environ.get("EIA_API_KEY", "0L1krdePYrx0Md6DNVesr53iVGqlGhfycwFyofwY")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")

MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "root")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "godigitaldb")

EXCEL_PATH = os.environ.get("EXCEL_PATH", "powerpulse_etl.xlsx")

# Logger Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("powerpulse_etl.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("PowerPulseETL")
