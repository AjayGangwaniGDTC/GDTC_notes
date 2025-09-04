'''This file is used to fetch the records from the api specified and if records
fetching is successfull it will return status code 200'''

import requests
from .config import EIA_API_KEY, logger
from .decorators import log_phase

@log_phase("Fetch EIA Data")
def fetch_data():
    '''This function is used to fetch the data'''
    #fetching the data from the below url
    url = "https://api.eia.gov/v2/electricity/state-electricity-profiles/capability/data/"
    #Giving parameters such as what will be the frequency and start and end date
    params = {
        "api_key": EIA_API_KEY,
        "frequency": "annual",
        "start": "2021",
        "end": "2023"
    }
    #Getting all the data from the url
    response = requests.get(url, params=params, timeout=10)
    #checking the status whether the data is correctly retrieved or not 200 is for success
    response.raise_for_status()
    #converting the data into json format
    data = response.json()
    #Extracting only the necessary information required by us
    record = data.get('response', {}).get('data', [])
    logger.info("Fetched %s records from EIA API.", len(record))
    return record
