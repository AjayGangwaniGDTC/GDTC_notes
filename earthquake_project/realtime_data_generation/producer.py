from faker import Faker
from datetime import datetime, timedelta
from confluent_kafka import Producer
import random
import json
import time

fake = Faker()
def generate_random_data():
    return {
        "id": fake.bothify(text='???######'),
        "date": datetime.utcnow().isoformat(),
        "latitude": float(fake.latitude()),
        "longitude": float(fake.longitude()),
        "magnitude": float(fake.pydecimal(min_value=0.0, max_value=10.0, right_digits=1))
    }
    
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message sent to topic {msg.topic()}[{msg.partition()}] offset{msg.offset()}")

config = {
    "bootstrap.servers": "localhost:29092"
    }
producer = Producer(config)

topic_name = 'realtime_earthquake_data'

end = datetime.utcnow() + timedelta(hours=2)

while datetime.utcnow() < end:
    record_count = random.randint(0, 5)
    
    for i in range(record_count):
        data = generate_random_data()
        producer.produce(
            topic = topic_name,
            value = json.dumps(data),
            callback=delivery_report
        )
        print(f"Data sent {data}")
        
    producer.flush()
    
    sleeptime = random.uniform(5, 15)
    time.sleep(sleeptime)