from faker import Faker
from kafka import KafkaProducer
import json, time
import random
import string

parent = \
    [
        {
            "x": random.uniform(500, 1000),
            "y": random.uniform(500, 1000),
            "width": random.randint(50, 1000),
            "height": random.randint(50, 1000)
        }
    ]

views = ["/dashboard", "/view", "/staff", "/vnface"]

types = ["Desktop1920", "Desktop1366", "Ipad", "Smartphone", "Other"]

y = [None, random.randint(500, 1000)]

timestamp = [1676687547526, 1677549864335, 1677482471687, None]

class Producer:
    def __init__(self, parent, views, types, y):
        self.parent = parent
        self.views = views
        self.types = types
        self.y = y

    def init_producer(self):
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9091', 'localhost:9092', 'localhost:9093'],
            value_serializer=self.json_serializer
        )
        return producer

    def generate_dummy_data(self, ux_click_id: int):
        return {
            "collection": random.randint(1, 10),
            "query": "insert",
            "data": {
                "events": [
                {
                    "key": "[CLY]_action",
                    "count": 1,
                    "segmentation": {
                        "type": "click",
                        "x": random.randint(500, 1000),
                        "y": self.y[random.randint(0, 1)],
                        "width": random.randint(1500, 2000),
                        "height": random.randint(1000, 2000),
                        "view": self.views[random.randint(0, len(views) - 1)],
                        "parent": self.parent[0],
                        "domain": "console-vnface.vnpt.vn"
                    },
                    "timestamp": 34324235233,
                    "hour": random.randint(4, 20),
                    "dow": random.randint(1, 10)
                }
            ],
            "app_key": "5fa32bd8282b2fcdc247b68241faebffcd4ece04",
            "device_id": str(ux_click_id),
            "sdk_name": "javascript_native_web","sdk_version": "22.06.0",
            "t": 1,
            "timestamp": timestamp[random.randint(0, len(timestamp) - 1)],
            "hour": random.randint(4, 20),
            "dow": random.randint(1, 10),
            "raw_html": None,
            "screen_size_type": self.types[random.randint(0, len(types) - 1)],
            "_id": ux_click_id
            }
        }

    @staticmethod
    def id_generator(
            size=24, chars=string.ascii_lowercase + string.digits
    ):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def json_serializer(data):
        return json.dumps(data).encode('utf-8')

    def generate_ux_data(self, init_index: int, topic: str, time_sleep: int):
        producer = self.init_producer()
        i = init_index
        while True:
            i += 1
            ux_click = self.generate_dummy_data(i)
            print("============================================================")
            print(ux_click)
            producer.send(topic=topic, value=ux_click)
            time.sleep(time_sleep)

if __name__ == '__main__':
    producer = Producer(parent, views, types, y)

    index = 0
    topic = "ux_data_exbe"
    time_sleep = 1
    producer.generate_ux_data(index, topic, time_sleep)
