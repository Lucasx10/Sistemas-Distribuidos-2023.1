import pika
from termcolor import colored

# Conecta ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara o tópico de incêndio
channel.queue_declare(queue='fire_alert')

# Define a função de callback para lidar com as mensagens recebidas
def callback(ch, method, properties, body):
    # Simula a ativação do alarme sonoro ou luminoso
    print(colored('Fogo Detectado! Ativando alarme de incêndio...', 'red'))

    # Publica uma mensagem indicando que o sistema de prevenção de incêndio deve ser ativado
    channel.basic_publish(exchange='', routing_key='fire_prevention_system', body='Ativar sistema de prevenção de incendio')
    print('Sistema de alarme de incendio ativado')

# Registra a função de callback no tópico de incêndio
channel.basic_consume(queue='fire_alert', on_message_callback=callback, auto_ack=True)

# Começa a consumir mensagens
channel.start_consuming()
