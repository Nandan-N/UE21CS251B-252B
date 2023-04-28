import socket
import tkinter as tk

# Define server IP address and port number
SERVER_IP = '192.168.106.228'
SERVER_PORT = 5555

def send_url():
    # Get the URL entered in the text box
    url = url_entry.get()

    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Send the URL to the server
    client_socket.send(url.encode())

    # Receive a response from the server
    response = client_socket.recv(1024).decode()

    # Update the output text box with the response from the server
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, response)

    client_socket.close()

# Create the main window
root = tk.Tk()
root.title('Web Monitoring Client')

# Create the input text box and label
url_label = tk.Label(root, text='Enter a URL:')
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the button to send the URL to the server
send_button = tk.Button(root, text='Send', command=send_url)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Create the output text box and label
output_label = tk.Label(root, text='Output:')
output_label.grid(row=2, column=0, padx=10, pady=10)
output_text = tk.Text(root, width=50, height=10)
output_text.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
