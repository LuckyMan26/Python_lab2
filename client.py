import socket

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    while True:
        # Get user input or command
        user_input = input("Enter command: ")
        # Send the input/command to the server
        s.sendall(user_input.encode())
        # Receive response from the server
        data = s.recv(1024)
        print('Received', repr(data))
