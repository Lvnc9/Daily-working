#!/usr/bin/python
# Start
# Hello my friend, i just named you friend cause that suites you
# Modules
import socket 

def respond(client):
    response = input("Enter a Value:")
    client.send(bytes(client, 'utf8'))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2401))
server.listen(1)

### This class decorates a socket object
# and presents the send and close interface to client sockets ###
class LogSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print(f"Sending {self.data} to {self.socket.getpeername()[0]}")
        self.socket.send(data)
    
    def close(self):
        self.socket.close()

try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()





# End