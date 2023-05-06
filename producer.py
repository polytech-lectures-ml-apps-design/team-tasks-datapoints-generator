import json
import os
import string
import logging
from random import random, choices
from time import time, sleep
from kafka import KafkaProducer
from dataclasses import dataclass, asdict


@dataclass
class DataPoint:
    tag_id: str
    timestamp: int
    value: float


data_freq = 1  # Hz

# tag list generation
tag_length = 7
num_tags = 10
tag_list = [''.join(choices(string.ascii_uppercase + string.digits, k=tag_length)) for _ in range(num_tags)]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("establishing connection to kafka")
producer = KafkaProducer(bootstrap_servers=os.environ['KAFKA_BOOTSTRAP_SERVERS'],
                         value_serializer=lambda x: json.dumps(asdict(x)).encode('utf-8'))
logging.info("connected to kafka, start publishing")

while True:
    for tag_id in tag_list:
        dp = DataPoint(tag_id, int(time()), random())
        producer.send('raw_data', dp)
        logging.debug(f"sent datapoint {dp}")
    # producer.flush()
    sleep(1/data_freq)

