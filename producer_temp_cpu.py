import pika
import psutil
import time

# Conecta ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara o tópico de temperatura
channel.queue_declare(queue='temperature')

def publish_temp_cpu():
    # Publica a temperatura da CPU no tópico
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    channel.basic_publish(exchange='', routing_key='temperature', body=str(temperature))

while True:
    publish_temp_cpu()
    time.sleep(5)
