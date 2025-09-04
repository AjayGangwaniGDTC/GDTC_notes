import json
from time import sleep 
import requests 
import pandas as pd 
from datetime import datetime, timedelta
from .vault_config import update_vault
class Data:
    response = update_vault()
    base_url = response['base_url']
    count_url = response['count_url']
    allowed_query_keys = { "format", "minlatitude", "maxlatitude", "minlongitude", "maxlongitude", "minmagnitude", "maxmagnitude", "eventtype", "orderby", "limit", "offset", "starttime", "endtime" }

    def __init__(self, config_path: str, max_retries=3, retry_delay=10):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.query_params = {k: v for k, v in self.config.items() if k in self.allowed_query_keys}
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def get_count(self, start_time, end_time):
        params = self.build_query(start_time, end_time)
        response = self.make_requests_with_retry(self.count_url, params)
        return response.get("count", 0)

    def get_dataframe(self, start_time, end_time):
        params = self.build_query(start_time, end_time)
        response = self.make_requests_with_retry(self.base_url, params)
        return self.parse_response(response)

    def build_query(self, start_time, end_time):
        query = self.query_params.copy()
        query["starttime"] = start_time.isoformat()
        query["endtime"] = end_time.isoformat()
        return query
    
    def make_requests_with_retry(self, url, params):
        attempt = 0
        while attempt < self.max_retries:
            try:
                response = requests.get(url, params=params, timeout=30)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                if response.status_code==429:
                    print(f"Rate limit Reached retrying in {self.retry_delay} seconds")
                    sleep(self.retry_delay)
                    attempt += 1
                else:
                    raise e
            except requests.exceptions.RequestException as e:
                print("Request failed: {e}. Retrying in {self.retry_delay} seconds")
                sleep(self.retry_delay)
                attempt += 1
        print("Maximum entries reached")
        return {}

    def parse_response(self, data):
        records = []
        for feature in data.get("features", []):
            props = feature["properties"]
            coords = feature["geometry"]["coordinates"]
            if props['time'] < 0:
                timestamp = datetime(1970, 1, 1) + timedelta(seconds=(props['time']/1000))
            else:
                timestamp = datetime.fromtimestamp(props['time']/1000)
            records.append({
                "id": feature["id"],
                "place": props.get("place"),
                "magnitude": props.get("mag"),
                "time": timestamp,
                "latitude": coords[1],
                "longitude": coords[0],
                "depth": coords[2],
                "is_tsunami": props.get("tsunami"),
                "status": props.get("status"),
                "type": props.get("type")
            })
        df = pd.DataFrame(records)
        df['time'] = df['time'].astype("datetime64[s]")
        return df  