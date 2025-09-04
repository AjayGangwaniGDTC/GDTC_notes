'''This file is used for converting the data from api into an excel sheet'''

import pandas as pd
from .config import EXCEL_PATH, logger
from .decorators import log_phase

@log_phase("Export to Excel")
def export_to_excel(data):
    '''function used to create dataframes from the api data and then converting 
    it to excel file'''
    #Creating the dataframes from the data
    df = pd.DataFrame(data)
    #Converting the dataframes into excel file
    df.to_excel(EXCEL_PATH, index=False)
    logger.info("Data exported to Excel at %s", EXCEL_PATH)
