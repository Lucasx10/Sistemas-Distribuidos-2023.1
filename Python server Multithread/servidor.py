import threading
import socket
import time
import psutil
import matplotlib.pyplot as plt

HOST = ''
PORT = 5000

clients = []

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((HOST, PORT))
        print(f'Servidor escutando na porta {PORT}...')
        s.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = s.accept()
        print(f'Conectado por {addr}')
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            # Mensagens de 1 byte, 512 bytes, 1KB, 10KB e 100KB
            sizes = [1, 512, 1024, 10240, 102400]

            for size in sizes:
                msg = b'a' * size
                start_time = time.time()
                msg_reversed = msg[::-1]  # Reverte a mensagem
                client.send(msg)  # Ecoa a mensagem de volta para o cliente
                broadcast(msg_reversed, client)  # Envia a mensagem revertida para outros clientes
                end_time = time.time()

                print(f"Tamanho da mensagem: {size} bytes, "
                      f"Tempo de resposta: {end_time - start_time:.4f} segundos")

            # Adiciona um delay de 1 segundo entre cada conjunto de mensagens
            time.sleep(1)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

def plot_cpu_memory_network():
    # Cria figuras para os gráficos
    fig, ax = plt.subplots(3)

    # Configura o título e as legendas dos gráficos
    fig.suptitle('Utilização de CPU, memória e rede')
    ax[0].set_ylabel('CPU (%)')
    ax[1].set_ylabel('Memória (%)')
    ax[2].set_ylabel('Rede (MB/s)')

    # Lista vazia para armazenar os valores de CPU, memória e rede
    cpu_usage = []
    memory_usage = []
    network_usage = []

    # Loop para atualizar os valores dos gráficos a cada segundo
    while True:
        # Obtém os valores de uso da CPU, memória e rede do sistema operacional
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        net_speed = psutil.net_io_counters().bytes_sent / (1024 ** 2)

        # Adiciona os valores à lista correspondente
        cpu_usage.append(cpu_percent)
        memory_usage.append(mem_percent)
        network_usage.append(net_speed)

        # Atualiza os gráficos com os valores mais recentes
        ax[0].plot(cpu_usage, color='blue')
        ax[1].plot(memory_usage, color='green')
        ax[2].plot(network_usage, color='red')

        # Limita o número de pontos dos gráficos a 100
        max_points = 100
        if len(cpu_usage) > max_points:
            ax[0].set_xlim(len(cpu_usage) - max_points, len(cpu_usage))
        if len(memory_usage) > max_points:
            ax[1].set_xlim(len(memory_usage) - max_points, len(memory_usage))
        if len(network_usage) > max_points:
            ax[2].set_xlim(len(network_usage) - max_points, len(network_usage))

        # Atualiza os gráficos
        plt.pause(1)

if __name__ == '__main__':
    # Inicia o servidor em uma thread separada
    server_thread = threading.Thread(target=main)
    server_thread.start()

    # Plota os gráficos de uso do sistema em uma thread separada
    plot_thread = threading.Thread(target=plot_cpu_memory_network)
    plot_thread.start()

    # Aguarda o encerramento das threads
    server_thread.join()
    plot_thread.join()
