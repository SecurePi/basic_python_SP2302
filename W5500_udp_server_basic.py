# udp_server_basic.py

import socket

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 5001        # Port to listen on

# Create UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))

print(f"[+] UDP Server listening on {HOST}:{PORT}")

try:
    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"[<] Received from {addr}: {data.decode()}")
        udp_socket.sendto(b"ACK: " + data, addr)

except KeyboardInterrupt:
    print("\n[!] UDP Server shutting down")

finally:
    udp_socket.close()
    print("[*] Socket closed")
