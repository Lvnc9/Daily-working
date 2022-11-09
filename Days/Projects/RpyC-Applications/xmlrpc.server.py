#!/usr/bin/env
# Start
# xmlrpc Server Module
# Modules
import datetime
import threading
import thread_safe_data_wrapper as rpyc
import rpyc
import sys
import MeterMt


PORT = 11003

Manager = MeterMt.Manager()


class MeterService(rpyc.Service):

    def on_connect(self): # When a connection is made to the service
        pass

    def on_disconnect(self):
        pass

    exposed_login = Manager.login
    exposed_get_status = Manager.get_status()
    exposed_get_job = Manager.get_job()
    

if __name__ == "__main__":
    import rpyc.utils.server
    print(f"Meter Server Startup at {datetime.datetime.now().isoformat()[:19]}")
    server = rpyc.utils.server.Thread.Server(MeterService, port=PORT)
    thread = threading.Thread(target=server.start)
    thread.start()
    try:
        if len(sys.argv) > 1: # NOTIFY IF CALLED BY A GUI CLIENT
            with open(sys.argv[1], "wb") as file:
                file.write(b"\n")
        thread.join()
    except KeyboardInterrupt:
        pass
    server.close()
    print(f"\rMeter server shutdown at {datetime.datetime.now().isoformat()[:19]}")
    MeterMt.Manager.dump()


# End