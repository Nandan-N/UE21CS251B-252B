import socket
import ast 

host = '10.30.202.57' 
port = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

data = client_socket.recv(8192)
availible_images = ast.literal_eval(data.decode())
#print(type(availible_images))

for i in range(len(availible_images)):
	print('{}	{}'.format(i+1, availible_images[i][:-4]))
	
index = int(input('\nEnter the index of the image to be downloaded: '))

if index not in [i for i in range(1,31)]:
	index = int(input('\nEnter index again, index should be in the range 1 - 30'))

# Send index value to the server
client_socket.send(str(index).encode())

# receive image data from server
image_data = b''
while True:
    chunk = client_socket.recv(8192)
    if not chunk:
        break
    image_data += chunk

print('Total bytes received: {}'.format(len(image_data)))

with open('{}'.format(availible_images[index-1]), 'wb') as f:
    f.write(image_data)

client_socket.close()