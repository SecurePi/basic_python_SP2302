import socket

# Define the host and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Set timeout for the server socket
server_socket.settimeout(60)  # Timeout set to 60 seconds

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on {}:{}'.format(HOST, PORT))

while True:
    try:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print('Connection from', client_address)

        # Receive data from client
        data = client_socket.recv(1024)

        if not data:
            break

        print('Received:', data.decode())

        # Send a response back to the client
        client_socket.sendall('Message received'.encode())

        # Close the connection with the client
        client_socket.close()

    except socket.timeout:
        print("No client connection for 60 seconds. Closing server socket.")
        break

# Close the server socket
server_socket.close()
