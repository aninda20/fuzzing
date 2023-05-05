import socket
import ssl
import hashlib

# Start a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 8000))
server_socket.listen(1)

# Wait for a client to connect
print("Waiting for a client to connect...")
client_socket, client_address = server_socket.accept()
print(f"Client connected from {client_address}")

# Wrap the socket with SSL/TLS
ssl_socket = ssl.wrap_socket(client_socket, server_side=True, keyfile="server.key",
                             certfile="server.crt", ssl_version=ssl.PROTOCOL_TLS)


while True:
    # Receive data from the client
    received_data = ssl_socket.recv(4096)
    print(f"Received data: {received_data.decode()}")

    # Compute the message digest of the received data
    hash_obj = hashlib.sha256()
    hash_obj.update(received_data)
    digest = hash_obj.digest()

    #  Send the digest to the client
    ssl_socket.sendall(digest)

# Close the sockets
ssl_socket.close()
server_socket.close()










