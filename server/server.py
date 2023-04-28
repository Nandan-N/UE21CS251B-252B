import socket
import requests
import validators

SERVER_IP = '192.168.106.228'
SERVER_PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(2)

print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()

    print(f"Client connected from {client_address}")

    # from the client
    data = client_socket.recv(1024).decode()
    print(f"Received data: {data}")

    # from requests to check status of urls
    url = data
    try:
        response = requests.get(url)
    except:
        message = f'{url} does not exist'
    # status to client
    else:
        status_code = response.status_code
        if status_code == 200:
            message = f"The website {url} is up and running with status code {status_code}"
        else:
            message = f"The website {url} is down with status code {status_code}"
            
    client_socket.send(message.encode())

    client_socket.close()