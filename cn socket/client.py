import threading
import socket
#how many clients can join?
#buffer size
alias = input('Choose an alias >>> ')#a
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.106.228', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "alias?":
                client.send(alias.encode('ascii'))
            else:
                print(message)
        except:
            print('ERROR! SERVER IS DOWN')
            client.close()
            break

def write():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()