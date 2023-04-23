import threading                    
import socket
import psutil                       #pip install psutil
import matplotlib.pyplot as plt     #pip install matplotlib

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
            data = client.recv(1024)  # Recebe a mensagem do cliente
            print("Requisições: ",len(clients))
            print(f"Tamanho msg: {len(data)} bytes")
            if not data:
                deleteClient(client)
                break
            msg = data.decode('utf-8')
            msg_reversed = msg[::-1]  # Reverte a mensagem
            broadcast(msg_reversed, client)  # Envia a mensagem para todos os clientes


        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg.encode('utf-8'))
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
    # Inicia o servidor
    server_thread = threading.Thread(target=main)
    server_thread.start()

    # Plota os gráficos de uso do sistema em uma thread separada
    plot_thread = threading.Thread(target=plot_cpu_memory_network)
    plot_thread.start()

    # Aguarda o encerramento das threads
    server_thread.join()
    plot_thread.join()