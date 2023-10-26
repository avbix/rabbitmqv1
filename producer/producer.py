# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Определяем имя exchange и тип (в данном случае "direct")
exchange_name = 'direct_logs'
exchange_type = 'direct'

# Объявляем exchange
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

# Определяем имя очереди
queue_name = 'my_queue'

# Объявляем очередь
channel.queue_declare(queue=queue_name)

# Привязываем очередь к exchange с определенным routing key
routing_key = 'info'  # Это может быть любой ключ, который соответствует маршрутизации
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Отправляем сообщение в exchange с указанным routing key
message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f"Sent: '{message}' with routing key '{routing_key}'")

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()
