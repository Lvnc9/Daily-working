#! python3.9.9
# Start
# Dont know what to write yet -> algorithme not designed yet amigo needs to command!
# Modules
from queue import Queue
from collections import defaultdict, namedtuple
import time

# TODO: Client -> an duck typing object that works internally
class Client(object):
    """ Purpose:
        ALl the requests will be get from here and store
        in a queue data structure for serving

        functionallity:
            """
    changed_clients = namedtuple('client', 'id name request')

    def __init__(self, clients:changed_clients):
        self.__clients = clients
        self.time = time.time()
    
    def __new__(self, cls):
        self.queue = Queue(maxsize=100)
        for item in self.__clients:
            self.queue.put(item, timeout=30)
            
    @property
    def working(self):
        print(f"you are Currently Watching {self.__clients}")
    
    @working.setter
    def working(self, client):
        print(f"Queing clients in {self.__clients}")
        self.__clients = client
    
    @working.deleter
    def working(self):
        print(F"YOU ARE ABOUT TO DELET THE WHOLE CLIENTS")
        print(F"ENTER 'Y' FOR DELTETING AND 'N' FOR NOT DLETING IT")
        answer = str(input('\n')).lower()
        if answer[0] is 'y':
            print("PROPERTY CLIENT HAS DELETED")
            del self.__clients



# All the requests are saving in a queue using FIFO-queue
 
# TODO: Server
# TODO:  
# End