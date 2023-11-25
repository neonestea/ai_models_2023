import pika
import os

amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)


connection = pika.BlockingConnection(url_params)
channel = connection.channel()
message = "info: Hello World!"


channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

channel.basic_publish(exchange='logs', routing_key='',
                       body=message, properties=pika.BasicProperties(delivery_mode=2))
print(f" [x] Sent {message}")


channel.close()
connection.close()