import socket
from musicstoredb import MusicStoreDB
from utils import Album, Artist, Genre

# Initialize the MusicStoreDB
db_file = 'musicstore.db'
music_store_db = MusicStoreDB(db_file)


# Define the process_request function to handle incoming requests
def process_request(request):
    # Decode the request data
    request = request.decode()
    # Split the request into command and arguments
    command, *args = request.split()

    # Process different types of requests
    if command == "ADD_ARTIST":
        # Example: ADD_ARTIST Eminem RAP
        name, genre = args
        artist = Artist(name, None, [], Genre[genre])
        music_store_db.add_artist(artist)
        return "Artist added successfully.".encode()
    elif command == "ADD_ALBUM":
        # Example: ADD_ALBUM "The Marshall Mathers LP" 1 18 1
        name, id, numberOfSongs, artist_id = args
        album = Album(name, int(id), int(numberOfSongs))
        # Retrieve the artist from the database based on the artist_id
        artist = music_store_db.get_artist_by_id(int(artist_id))
        album.artist = artist
        music_store_db.add_album(album)
        return "Album added successfully.".encode()
    # Add more elif clauses for other types of requests (update, delete, retrieve, etc.)

    else:
        return "Invalid command.".encode()


# Server configuration
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()

    # Accept connections
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # Receive data from the client
                data = conn.recv(1024)
                if not data:
                    break
                # Process the received data using process_request function
                response = process_request(data)
                # Send the response back to the client
                conn.sendall(response)
