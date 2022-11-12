#!/usr/bin/python3
# Start
# Client side of app
# Modules
import rpyc
import thread_safe_data_wrapper as MeterMt


manager = MeterMt()

def main():
    username, password = manager.login()
    if username is not None:
        try:
            service = rpyc.connect(HOST, PORT) 
            manager = service.root‍‍‍
            sessionId, name = manager.login(username, password)
            print(f"welcome, {name}, to meter RPYC")
            interact(manager, sessionId)
        except ConnectionError as err:
            print(f"Error: Is the meter server running? {err}")


# End