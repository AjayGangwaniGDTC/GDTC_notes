from confluent_kafka import Consumer, KafkaException
from queue import Queue
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import json
import pandas as pd
import threading

# engine = create_engine("postgresql://postgres:admin123@localhost:5432/postgres") 
class KafkaConsumerRealtime:
    def __init__(self, topic='realtime_earthquake_data', max_records=5, run_hours=2):
        self.data_queue = Queue(maxsize=max_records)
        self.consumer = Consumer({
            'bootstrap.servers': 'localhost:29092',
            'auto.offset.reset': 'latest',
            'group.id': 'dashboard-consumer' 
            })
        self.consumer.subscribe(['realtime_earthquake_data'])
        self.running = False
        self.run_hours = run_hours
        
    def consume_kafka(self):
        end = datetime.utcnow() + timedelta(hours=self.run_hours)

        try:
            while self.running and datetime.utcnow() < end:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"Kafka Error {msg.error()}")
                    continue 
                try:
                    data = json.loads(msg.value().decode('utf-8'))
                    print(f"Received JSON message: {data}")
                    if self.data_queue.full():
                        self.data_queue.get()
                    self.data_queue.put(data)
                    
                    # df = pd.DataFrame([data])
                    # df.to_sql("realtime_earthquakes", engine, if_exists="append", index=False)
                except Exception as e:
                    print(f"kafka parse error: {e}")
                    continue
                            
                
                
                # print(list(self.data_queue.queue))
        except KeyboardInterrupt:
            print("Consumer stopped by user")  
        finally:     
            self.stop()
            
    def start(self):
        if not self.running:
            self.running=True
            threading.Thread(target=self.consume_kafka, daemon=True).start()

    def stop(self):
        self.running = False
        self.consumer.close()
        
    def get_data(self):
        return list(self.data_queue.queue)