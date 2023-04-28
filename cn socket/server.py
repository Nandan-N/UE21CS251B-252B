import threading
import socket
host = '192.168.106.228'#'192.168.1.2'  # bind to the local network IP address
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
            print(message.decode('ascii'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('ascii'))
            aliases.remove(alias)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'connection is established with {str(address)}')

        client.send('alias?'.encode('ascii'))
        alias = client.recv(1024).decode('ascii')
        aliases.append(alias)
        clients.append(client)

        print(f'The alias of this client is {alias}')
        broadcast(f'{alias} has connected to the chat room'.encode('ascii'))
        client.send('you are now connected!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()