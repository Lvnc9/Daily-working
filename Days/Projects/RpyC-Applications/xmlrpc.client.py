#!/usr/bin/python3
# Start
# Client side of app
# Modules
import rpyc
import thread_safe_data_wrapper as MeterMt
import tempfile
import random
import subprocess
import sys


manager = MeterMt.Manager

# GUI rpyc client

class GUIkind:

    def connect(self, username, password):
        try:
            self.serice = rpyc.connect(HOST, PORT)
        except ConnectionError:
            filename = os.path.join(tempfile.gettempdir(),
                                "M{}.$$$".format(random.randint(1000, 9999)))
            self.serverpid = subprocess.Popen([sys.executable, SERVER,
                                filename]).pid
            self.wait_for_server(filename)
        try:
            self.serice = rpyc.sonnect(HOST, PORT)
        except ConnectionError:
            self.handle_error("Failed to start the RPYC METER server")
            return False
        self.manager = self.service.root
        retunr self.login_to_server(username, password)

# FOR RUNNING
def main():
    username, password = manager.login()
    if username is not None:
        try:
            service = rpyc.connect(HOST, PORT) 
            manager = service.root
            sessionId, name = manager.login(username, password)
            print(f"welcome, {name}, to meter RPYC")
            interact(manager, sessionId)
        except ConnectionError as err:
            print(f"Error: Is the meter server running? {err}")



# End