# tcp_client_basic.py

import socket

# === Configuration ===
SERVER_IP = '10.0.1.202'  # Replace with your server's IP address
PORT = 5000              # Replace with the server's port

# === Create TCP socket ===
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_IP, PORT))
    print(f"[+] Connected to {SERVER_IP}:{PORT}")

    # Send a message
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    print(f"[>] Sent: {message}")

    # Receive response
    response = client_socket.recv(1024)
    print(f"[<] Received: {response.decode()}")

except Exception as e:
    print(f"[!] Error: {e}")

finally:
    client_socket.close()
    print("[*] Connection closed")
