Please find files attached generated files attached in the folder server.crt and server.key , it should be in the same folder as Alice.py and Bob.py. 
Right mouse click and copy path of these files and attach it paste it in the section socket wrap using SSL/TLS.

Here is example of my program:

# Wrap the socket with SSL/TLS
ssl_socket = ssl.wrap_socket(client_socket, server_side=True, keyfile="C:/Users/ashis/OneDrive/Desktop/Info security/Project-1/server.key", certfile="C:/Users/ashis/OneDrive/Desktop/Info security/Project-1/server.crt", ssl_version=ssl.PROTOCOL_TLS)

File path of server.key should be added in keyfile.
File path of server.crt should be added in cerfile.

Same procedure for alice.py and bob.py

And lastly execute Alice.py first and then Bob.py next.