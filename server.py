import socket
import os 

hostname = socket.gethostname()
#ip_address = socket.gethostbyname(hostname)
		
host = ''
port = 8000 
print("ip address: {}".format(host))

availible_images = os.listdir(r'images')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print('Server listening on', (host, port))


while True:
	client_socket, client_address = server_socket.accept()
	print('\n\nReceived connection from', client_address)

	#send available images
	message = '{}'.format(availible_images)
	client_socket.send(message.encode())

	#receive data from the client
	data = client_socket.recv(8192)
	print('Received image index from client:', data.decode())
	print('Image to be sent: {}'.format(availible_images[int(data.decode())-1]))
	
	#send image 
	with open(r'images/{}'.format(availible_images[int(data.decode())-1]), 'rb') as f:
		image_data = f.read()
        
	print('Image size: {} bytes'.format(len(image_data)))
    
	client_socket.sendall(image_data)
	client_socket.close()
















