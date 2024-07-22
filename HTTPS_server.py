from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

# Define the HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, HTTPS!")

# Server settings
host = '10.0.1.149'
port = 8443

# Generate SSL context
server_cert = 'server.crt'  # Path to your server certificate
server_key = 'server.key'  # Path to your server private key
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.load_cert_chain(server_cert, server_key)

# Create HTTPS server
https_server = HTTPServer((host, port), RequestHandler)

# Wrap the socket with SSL
https_server.socket = ssl_context.wrap_socket(https_server.socket)

# Start the server
print(f"Starting HTTPS server on {host}:{port}")
https_server.serve_forever()
