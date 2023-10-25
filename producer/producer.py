# Import the 'pika' library for RabbitMQ communication.
import pika

# Import the 'os' library to access environment variables.
import os

# Retrieve the AMQP URL from the environment variables.
amqp_url = os.environ['AMQP_URL']

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters(amqp_url)

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

# Create a channel for communication.
chan = connection.channel()

# Declare three queues named 'A', 'B', and 'C'.
chan.queue_declare(queue='A')
chan.queue_declare(queue='B')
chan.queue_declare(queue='C')

# Publish messages to the queues.
chan.basic_publish(exchange='', routing_key='A', body='Hello-A!')
chan.basic_publish(exchange='', routing_key='B', body='Hello-B!')
chan.basic_publish(exchange='', routing_key='B', body='Hello-B2!')
chan.basic_publish(exchange='', routing_key='C', body='Hello-C!')

# Print a message to indicate that the messages have been produced.
print("Produced the message")

# Close the channel.
chan.close()

# Close the connection to RabbitMQ.
connection.close()
