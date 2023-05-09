import sys
import socket
import threading
import base64

HOST = 'localhost'
PORT = 5000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except:
        return print('\nNão foi possível se conectar ao servidor!\n')

    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client])

    thread1.start()
    thread2.start()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048)
            if not msg:
                break
            else:
                decoded_msg = base64.b64decode(msg).decode('ascii')
                sys.stdout.write('\033[K' + decoded_msg + '\r\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> para continuar...')
            client.close()
            break

def sendMessages(client):
    while True:
        try:
            message = input().encode('ascii')
            if not message:
                client.close()
                break
            base64_bytes = base64.b64encode(message)
            client.sendall(base64_bytes)
        except:
            return

main()
