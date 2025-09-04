'''This file is used to gather all the elements of the project and create a
pipeline so everything works correctly'''

from .eia_client import fetch_data
from .mongo_store import store_to_mongo
from .excel_exporter import export_to_excel
from .mysql_loader import load_to_mysql
from .config import logger

#creating a class to execute all the project files
class PowerPulseETL:
    '''Creating a class so that everything is kept grouped together'''
    def run(self):
        '''This function is running all the components of the project'''
        logger.info("Starting PowerPulse ETL pipeline")
        data = fetch_data()
        export_to_excel(data)
        store_to_mongo(data)
        load_to_mysql(data)
        logger.info("PowerPulse ETL pipeline completed successfully")

if __name__ == "__main__":
    etl = PowerPulseETL()
    etl.run()
