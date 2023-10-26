# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

# Create a channel for communication.
chan = connection.channel()

# Declare three queues named 'A', 'B', and 'C'.
chan.queue_declare(queue='A')


# Publish messages to the queues.
chan.basic_publish(exchange='', routing_key='A', body='Hello-A!')

# Print a message to indicate that the messages have been produced.
print("Produced the message")

# Close the channel.
chan.close()

# Close the connection to RabbitMQ.
connection.close()
