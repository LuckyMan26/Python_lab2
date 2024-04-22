import socket

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Function to send requests to the server and receive responses
def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((HOST, PORT))
        # Send the request to the server
        s.sendall(request.encode())
        # Receive response from the server
        response = s.recv(1024)
        return response.decode()

# Test the server by sending some sample requests
if __name__ == "__main__":
    # Example requests
    requests = [
        "ADD_ARTIST Eminem RAP",
        "ADD_ALBUM 'The Marshall Mathers LP' 1 18 1",
        # Add more requests as needed
    ]

    # Send each request and print the response
    for request in requests:
        response = send_request(request)
        print(f"Request: {request}\nResponse: {response}")
