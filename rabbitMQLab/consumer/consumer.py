import pika
import time
import os

amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(url_params)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)


result = channel.queue_declare(queue='', exclusive=True, durable=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print(" [*] Waiting for logs.")

def callback(ch, method, properties, body):
    time.sleep(2)
    print(f' [x] {body}')
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)


channel.basic_consume(queue=queue_name,
                   on_message_callback=callback)



channel.start_consuming()