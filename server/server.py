import socket
import threading
import sys

def handle_client(connection):
    #Handle a client connection by receiving data from the client, updating the 'notes.txt' file, and sending a response back to the client.
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break  # Exit the loop if no data is received, indicating the client has disconnected
        
        print(f"Received data: {data}")
        with open('notes.txt', 'w') as f:
            f.write(data)
        
        response = "Notes updated successfully."
        connection.send(response.encode())
    
    connection.close()

import socket
import threading

def server():
    #Starts a server that listens for incoming connections and handles them in separate threads.
    host = socket.gethostname()
    port = 3333
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server is listening. Type 'exit' to close.")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
    server_socket.close()

# Start the server in a separate thread
server_thread = threading.Thread(target=server)
server_thread.start()

# CLI for the server
while True:
    command = input()
    if command.lower() == 'exit': #only accepts 'exit' a command to close the server
        print("Shutting down the server.")
        sys.exit()