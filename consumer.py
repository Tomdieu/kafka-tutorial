from time import sleep

from kafka import KafkaConsumer
from json import loads
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def consume(topics: list[str]):
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                             enable_auto_commit=False, group_id='consumer-group-1',
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    consumer.subscribe(topics=topics)

    while True:

        message = consumer.poll(2000)

        if message:

            if message is None:
                continue

            for topic, messages in message.items():

                for msg in messages:

                    print(f"Message: {msg.value}")
                    print(f"Topic: {msg.topic}")
                    print(f"Partition: {msg.partition}")
                    print(f"Offset: {msg.offset}")
                    print(f"Key: {msg.key}")
                    print(f"Timestamp: {msg.timestamp}")

        sleep(10)

    # for message in consumer:
    #
    #     print(message.value)
    #     print(f"Message: {message.value}")
    #     print(f"Topic: {message.topic}")
    #     print(f"Partition: {message.partition}")
    #     print(f"Offset: {message.offset}")
    #     print(f"Key: {message.key}")
    #     print(f"Timestamp: {message.timestamp}")

    sleep(5)

    logging.info(" [ + ] Stared Consuming...")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python consumer.py <topic1> <topic2> ...")
        sys.exit(1)

    topics = sys.argv[1:]

    consume(topics)