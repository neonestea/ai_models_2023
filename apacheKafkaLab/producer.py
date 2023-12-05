import os
import time
import random
from kafka import KafkaProducer
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "my_topic")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.5.2")
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
)
i = 0
message = 'Hello, Kafka!'

producer.send(
        KAFKA_TOPIC_TEST,
        b'main Hello, Kafka!',
    )

print(f" [x] Sent main Hello, Kafka!")
producer.send(
        KAFKA_TOPIC_TEST,
        b'retry Hello, Kafka!',
    )
print(f" [x] Sent retry Hello, Kafka!")

producer.send(
        KAFKA_TOPIC_TEST,
        b'error Hello, Kafka!',
    )
print(f" [x] Sent error Hello, Kafka!")
producer.flush()
