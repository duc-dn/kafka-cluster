from kafka import KafkaConsumer
from pprint import pprint


consumer = KafkaConsumer(
    'ux_data_exbe', 
    auto_offset_reset='earliest',
    bootstrap_servers=['localhost:9093']
)
for message in consumer:
    pprint(message)
