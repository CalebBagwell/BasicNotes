import socket

def server():

    host = socket.gethostname()
    
    port = 3333
    
    s = socket.socket()
    
    s.bind((host, port))
    
    s.listen(2)
    
    c, address = s.accept()
    
    while True:
    
        data = c.recv(1024).decode()

        if not data:
            break
            
        print(f"Received from client: {data}")

        response = input("Enter response to send to client: ")
        
        c.send(response.encode())

    c.close()