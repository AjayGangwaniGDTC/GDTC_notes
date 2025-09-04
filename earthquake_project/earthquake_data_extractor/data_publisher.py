import os 
import pandas as pd 
from datetime import datetime 
from sqlalchemy import create_engine 
from confluent_kafka import Producer

class DataPublisher: 
    def __init__(self, output_dir="data", write_to_parquet=True, write_to_postgres=False, write_to_kafka=False, kafka_topic="earthquake_data", kafka_config=None, postgres_url=None):
        self.output_dir = output_dir
        self.write_to_parquet = write_to_parquet
        self.write_to_postgres = write_to_postgres
        self.write_to_kafka = write_to_kafka
        self.kafka_topic = kafka_topic
        self.kafka_config = kafka_config or {}
        self.postgres_url = postgres_url

        if self.write_to_kafka:
            self.kafka_producer = Producer(self.kafka_config)

        if self.write_to_postgres and self.postgres_url:
            self.pg_engine = create_engine(self.postgres_url)

        os.makedirs(self.output_dir, exist_ok=True)

    def publish(self, df: pd.DataFrame):
        if df.empty:
            print("No data to publish.")
            return

        if self.write_to_parquet:
            self.write_parquet(df)

        if self.write_to_postgres:
            self.write_postgres(df)

        if self.write_to_kafka:
            self.write_kafka(df)

    def write_parquet(self, df):
        df["year"] = df["time"].dt.year
        for year, group in df.groupby("year"):
            filepath = os.path.join(self.output_dir, f"{year}.parquet")

            if os.path.exists(filepath):
                existing = pd.read_parquet(filepath)
                group = pd.concat([existing, group], ignore_index=True).drop_duplicates(subset=["id"])

            group.to_parquet(filepath, index=False)
            print(f"Parquet saved: {filepath}")

    def write_postgres(self, df):
        try:
            df.to_sql(
                name="earthquake_data",
                con=self.pg_engine,
                if_exists="append",
                index=False,
                method="multi"
            )
            print("Written to PostgreSQL.")
        except Exception as e:
            print("Failed to write to PostgreSQL:", e)

    def write_kafka(self, df):
        for _, row in df.iterrows():
            msg = row.to_json()
            self.kafka_producer.produce(self.kafka_topic, value=msg)
        self.kafka_producer.flush()
        print(f"Sent to Kafka topic: {self.kafka_topic}")