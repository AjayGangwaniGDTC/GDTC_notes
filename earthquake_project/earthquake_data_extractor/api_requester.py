import os 
import json 
import time 
from datetime import datetime, timedelta 
from .extract_data import Data 
from .data_publisher import DataPublisher

class APIRequester: 
    def __init__(self, config_path="query_config.json", checkpoint_file="checkpoint.txt"): 
        with open(config_path, "r") as f: 
            self.config = json.load(f)
            
        self.mode = self.config["type"]
        self.period = int(self.config.get("query_period_minutes", 5))
        self.buffer = int(self.config.get("query_buffer_minutes", 5))
        self.checkpoint_file = checkpoint_file
        self.rate_limit = 20000
        self.chunk_days = 10

        self.data_fetcher = Data(config_path)
        self.publisher = DataPublisher(
            write_to_parquet=True,
            write_to_postgres=False,
            write_to_kafka=False,
            kafka_topic="earthquake_data",
            kafka_config={"bootstrap.servers": "localhost:29092"},
            postgres_url="postgresql://postgres:admin123@localhost:5432/postgres"
        )

    def run(self):
        if self.mode == "historic":
            self.run_historic()
        elif self.mode == "realtime":
            self.run_realtime()
        else:
            raise ValueError("Unsupported mode in config.")

    def run_historic(self):
        checkpoint = self.load_checkpoint()
        start = checkpoint if checkpoint else datetime.fromisoformat(self.config["starttime"])
        end = datetime.fromisoformat(self.config["endtime"])

        while start < end:
            chunk_end = min(start + timedelta(days=self.chunk_days), end)
            count = self.data_fetcher.get_count(start, chunk_end)

            if count >= self.rate_limit:
                print(f"Count {count} exceeds limit.")
                self.recursive_split(start, chunk_end)
            else:
                df = self.data_fetcher.get_dataframe(start, chunk_end)
                self.publisher.publish(df)

            self.save_checkpoint(chunk_end)
            start = chunk_end

    def run_realtime(self):
        print("Running in realtime")
        while True:
            end = datetime.utcnow()
            start = end - timedelta(minutes=self.period)
            df = self.data_fetcher.get_dataframe(start, end)
            self.publisher.publish(df)
            print(f"Sleeping {self.buffer} minutes...")
            time.sleep(self.buffer * 60)

    def recursive_split(self, start, end):
        if (end - start).days <= 1:
            print(f"Cannot split further: {start} to {end}")
            return

        mid = start + (end - start) / 2
        left_count = self.data_fetcher.get_count(start, mid)

        if left_count >= self.rate_limit:
            self.recursive_split(start, mid)
        else:
            df = self.data_fetcher.get_dataframe(start, mid)
            self.publisher.publish(df)

        right_count = self.data_fetcher.get_count(mid, end)

        if right_count >= self.rate_limit:
            self.recursive_split(mid, end)
        else:
            df = self.data_fetcher.get_dataframe(mid, end)
            self.publisher.publish(df)

    def load_checkpoint(self):
        if os.path.exists(self.checkpoint_file):
            with open(self.checkpoint_file, "r") as f:
                return datetime.fromisoformat(f.read().strip())
        return None

    def save_checkpoint(self, dt):
        with open(self.checkpoint_file, "w") as f:
            f.write(dt.isoformat())