import socket
import threading  # Import threading for handling multiple clients

# Function to handle each client connection
def handle_client(connection, address):
    print(f"Connected to {address}")
    
    while True:
        # Receive data from the client
        data = connection.recv(1024)
        if not data:  # If no data is received, the client has closed the connection
            break
        print(f"Received from {address}: {data.decode()}")
        
        # Send a response back to the client
        connection.sendall(b"Hello, Client!")
    
    # Close the client connection
    print(f"Connection to {address} closed")
    connection.close()

# Main server function
def start_server():
    # Create a TCP/IP socket using IPv4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to localhost at port 12345
    server_socket.bind(('localhost', 12345))
    
    # Start listening for incoming connections
    server_socket.listen()
    print("Server is listening...")
    
    while True:
        # Accept a new connection
        connection, address = server_socket.accept()
        
        # Create a new thread for handling the client
        client_thread = threading.Thread(target=handle_client, args=(connection, address))
        client_thread.start()

# Start the server
if __name__ == "__main__":
    start_server()
