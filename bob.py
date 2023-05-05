import socket
import ssl
import hashlib

# Start a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 8000))
print("Connected to the server.")

# Wrap the socket with SSL/TLS
ssl_socket = ssl.wrap_socket(client_socket, keyfile="server.key",
                             certfile="server.crt", ssl_version=ssl.PROTOCOL_TLS)

while True:
    # Send data to the server
    data_to_send = "Hello Good Morning".encode()
    ssl_socket.sendall(data_to_send)

    # Receive the message digest from the server
    digest = ssl_socket.recv(32)

    # Compute the message digest of the sent data
    hash_obj = hashlib.sha256()
    hash_obj.update(data_to_send)
    expected_digest = hash_obj.digest()

    # Compare the expected digest with the received digest to verify integrity
    if digest == expected_digest:
        print("Data integrity verified.")
    else:
        print("Data has been tampered with.")

# Close the sockets
ssl_socket.close()
client_socket.close()
