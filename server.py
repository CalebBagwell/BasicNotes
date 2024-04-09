import socket
import threading
import sys

def handle_client(connection):
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
    print("Client connection closed.")

def server():
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
    if command.lower() == 'exit':
        print("Shutting down the server.")
        sys.exit()