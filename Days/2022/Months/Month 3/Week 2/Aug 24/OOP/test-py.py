#!/usr/bin/python
# using py.test for as the tester proccessor and using function argumants
# we user funcargs to assure there are some values which are set before the 
# test begins so we use them to make some configuration
# but we can set them to another file 
# Start 
import socket
import subprocess
import time


def pytest_funcarg_echoserver(request):
    def setup():
        p = subprocess.Popen(
            ['python3', 'tset.py'])
        time.sleep(1)
        return p
    
    def cleanup(p):
        p.terminate()
    
    return request.cached_setup(
        setup=setup,
        treardown=cleanup,
        scope="session",)

def pytest_funcarg_clientsocket(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 1028))
    request.addfinalizer(lambda:s.close())
    return s 

def test_echo(echoserver, clientsocket):
    clientsocket.send(b"laar")
    assert clientsocket.recv(3) == b"laar"

def test_echo2(echoserver, clientsocket):
    clientsocket.send(b"molaaar")
    assert clientsocket.recv(3) == b"molaaar"



# End