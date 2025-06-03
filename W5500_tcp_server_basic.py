# tcp_server_basic.py

import socket

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 5000        # Port to listen on

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] TCP Server listening on {HOST}:{PORT}")

try:
    conn, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[<] Received: {data.decode()}")
        conn.sendall(b"ACK: " + data)

except KeyboardInterrupt:
    print("\n[!] Server shutting down")

finally:
    conn.close()
    server_socket.close()
    print("[*] Connection closed")
