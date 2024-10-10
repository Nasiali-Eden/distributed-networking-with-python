import socket  # Import the socket module for network communication

# Create a TCP/IP socket using IPv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server running on localhost at port 12345
client_socket.connect(('localhost', 12345))

# Send a message to the server (in bytes format)
client_socket.sendall(b"Hello, Server!")

# Receive a response from the server, up to 1024 bytes
data = client_socket.recv(1024)

# Decode and print the response from the server (assuming it's in UTF-8 format)
print(f"Received from server: {data.decode()}")

# Close the socket after the communication is finished
client_socket.close()
