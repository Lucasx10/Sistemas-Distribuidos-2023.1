import socket
import threading
import base64

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
            msg = client.recv(2048)
            if not msg:
                deleteClient(client)
                break
            decoded_message = client.getpeername()[0] + ': ' + base64.b64decode(msg).decode('ascii')
            encoded_message = base64.b64encode(decoded_message.encode('ascii'))
            print(encoded_message)
            print(decoded_message)
            broadcast(encoded_message, client)
        except:
            deleteClient(client)
            break

def broadcast(msg, sender_client):
    for clientItem in clients:
        if clientItem != sender_client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)

main()
