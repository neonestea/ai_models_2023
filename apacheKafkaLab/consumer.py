import os
from kafka import KafkaConsumer, KafkaProducer
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC_TEST = os.environ.get("KAFKA_TOPIC_TEST", "my_topic")
KAFKA_API_VERSION = os.environ.get("KAFKA_API_VERSION", "7.5.2")
KAFKA_CONSUMER_GROUP = os.environ.get("KAFKA_API_VERSION", "my-test-group")


consumer = KafkaConsumer(
    KAFKA_TOPIC_TEST,
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=KAFKA_CONSUMER_GROUP,
)

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
    api_version=KAFKA_API_VERSION,
)

for message in consumer:
    message = message.value.decode("utf-8")
    print(f'[received] {message}')
    if 'main' in message:
        pass
    elif 'retry' in message:
        producer.send('retry-topic', bytes(message, 'utf-8'),)
        print(f'[Retry] {message}')
    elif 'error' in message:
        producer.send('dead-letter-topic', bytes(message, 'utf-8'),)
        print(f'[DLT] {message}')


