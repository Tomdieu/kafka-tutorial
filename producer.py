import logging
from kafka import KafkaProducer
from typing import Any
import json

logging.basicConfig(level=logging.DEBUG)


def publish(topic: str, event_type: str, body: Any):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    data = {
        'type': event_type,
        'data': body
    }

    producer.send(topic, value=data, key=bytes(event_type, encoding='utf-8'))
    producer.flush()

    logging.info(" [+] Message Published : ", json.dumps(data, indent=4))
