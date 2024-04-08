import socket

import socket

def server():
    #This function starts a server that listens for incoming connections from clients.
    #It receives data from the client, prints it, and sends a response back to the client.

    host = socket.gethostname()
    port = 3333
    
    # Create a socket object
    s = socket.socket()
    
    # Bind the socket to a specific address and port
    s.bind((host, port))
    
    # Listen for incoming connections
    s.listen(2)
    
    # Accept a connection from a client
    c, address = s.accept()
    
    while True:
        # Receive data from the client
        data = c.recv(1024).decode()

        if not data:
            break
            
        # Print the received data
        print(f"Received from client: {data}")

        # Get user input for the response to send to the client
        response = input("Enter response to send to client: ")
        
        # Send the response back to the client
        c.send(response.encode())

    # Close the connection
    c.close()