#!/usr/bin/python
# Start
# Working on decorators
# sending data to a socket and saving it
# Modules
import sys
import gzip
from io import BytesIO
import socket

class LoggingSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print("Sending {0} to {1}".format(
            data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()

class GzipSocket():
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())
    def close(self):
        self.socket.close()
        client, addr = server.accept()
        if log_send:
            client = LoggingSocket(client)
        if client.getpeername()[0] in compress_hosts:
            client = GzipSocket(client)
            respond(client)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost',2401))

server.listen(1)
# End