import pika
import os

amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(url_params)
chan = connection.channel()

chan.queue_declare(queue='A')
chan.queue_declare(queue='B')
chan.queue_declare(queue='C')

chan.basic_publish(exchange='', routing_key='A', body='Hello-A!')
chan.basic_publish(exchange='', routing_key='B', body='Hello-B!')
chan.basic_publish(exchange='', routing_key='B', body='Hello-B2!')
chan.basic_publish(exchange='', routing_key='C', body='Hello-C!')
print("Produced the message")

chan.close()
connection.close()
