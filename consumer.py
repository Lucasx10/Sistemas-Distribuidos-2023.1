import pika
from termcolor import colored

# Conecta ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara o tópico de temperatura e o tópico de incêndio
channel.queue_declare(queue='temperature')
channel.queue_declare(queue='fire_alert')

# Define a função de callback para lidar com as mensagens recebidas
def callback(ch, method, properties, body):
    temperature = float(body)
    if temperature > 50:
        # Se a temperatura for maior que 70 graus Celsius, publica uma mensagem no tópico de incêndio
        channel.basic_publish(exchange='', routing_key='fire_alert', body='FIRE DETECTED!')
        print(colored('Incedio detectado!','red'))
    else:
        print('Temperature:', temperature)

# Registra a função de callback no tópico de temperatura
channel.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=True)

# Inicia o loop de espera por mensagens
print('Aguardando tarefas...')
channel.start_consuming()
