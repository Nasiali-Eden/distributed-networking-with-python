import socket  # Import the socket module for network communication

# Create a TCP/IP socket using IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the localhost at port 12345
server_socket.bind(('localhost', 12345))

# Start listening for incoming connections (default queue size is set by the OS)
server_socket.listen()

print("Server is listening...")

# Wait for a client to connect, blocking call until a connection is established
# Returns a new socket object for communication with the client and the client's address
connection, address = server_socket.accept()
print(f"Connection from {address}")  # Display the client's address

# Receive data from the client, up to 1024 bytes
data = connection.recv(1024)

# Decode and print the received data (assuming it's in UTF-8 format)
print(f"Received data: {data.decode()}")

# Send a response back to the client
connection.sendall(b"Hello, Client!")  # Send a byte message

# Close the connection with the client
connection.close()

# Close the server socket, no longer accepting connections
server_socket.close()
