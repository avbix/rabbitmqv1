# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# ���������� ��� exchange � ��� (� ������ ������ "direct")
exchange_name = 'direct_logs'
exchange_type = 'direct'

# ��������� exchange
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

# ���������� ��� �������
queue_name = 'my_queue'

# ��������� �������
channel.queue_declare(queue=queue_name)

# ����������� ������� � exchange � ������������ routing key
routing_key = 'info'  # ��� ����� ���� ����� ����, ������� ������������� �������������
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# ���������� ��������� � exchange � ��������� routing key
message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f"Sent: '{message}' with routing key '{routing_key}'")

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()
