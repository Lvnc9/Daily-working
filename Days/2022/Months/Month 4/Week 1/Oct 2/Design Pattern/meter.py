#!/usr/bin/python
# Start
# NETWORKING
# Modules
import argparse
import random
import sys
import xmlrpc
import collections
import hashlib
import datetime
import sys
import datetime 

_User = collections.namedtuple("User", "username, sha256")
Reading = collections.namedtuple("Reading", "when reading reason username")

HOST = "localhost"
PORT = 11002
PATH = "/meter"

def handle_arguments():
    parser = argparse.ArgumentParser(conflict_handler="resolve")
    parser.add_argument("-h", "--host", default=HOST, type=str,
                        help="hosname [default %(default)s")
    parser.add_argument("-p", "--port", default=PORT, type=int,
                        help="port number [default %(defaults)d")
    parser.add_argument("--notify", help="specify a notification file")
    args = parser.parse_args()
    return args.host, args.port, args.notify

class Error(Exception): pass


def name_for_credentials(username, password):
    sha = hashlib.sha256()
    sha.update(password.encode("utf-8"))
    user = _User(username, sha.hexdigest())
    return _Users.get(user)


class Manager:
    """ saves meter readings and provide methods for logging
    and acquire jobs and saves results """

    SessionId = 0
    UsernameForSessionId = {}
    ReadingForMeter = {}

    def login(self, username, password):
        name = name_for_credentials(username, password)
        if name is None:
            raise Error("invalid username or password")
        Manager.SessionId += 1
        sessionId = Manager.SessionId
        Manager.UsernameForSessionId[sessionId] = username
        return sessionId, name


    def get_job(self, sessionId):
        self._username_for_sessionId(sessionId)
        while True: # Create fake meter
            kind = random.choice("GE")
            meter = "{}{}".format(kind, random.randint(40000,
                    99999 if kind == "G" else  999999))
            if meter not in Manager.ReadingForMeter:
                Manager.ReadingForMeter[meter] = None
                return meter

    def _username_for_sessionId(self, sessionId):
        try:
            return Manager.UsernameForSessionId[sessionId]
        except KeyError:
            raise Error("Invalid session ID")

    def submit_reading(self, sessionId, meter, when, reading, reason=""):
        if isinstance(when, xmlrpc.client.DateTime):
            when = datetime.datetime.strptime(when.value,
                            "%Y%M%D%T%H:%M%S")
        if (not isinstance(reading, int) or reading < 0) and not reason:
            raise Error("Invalid reading")
        
        if meter not in Manager.ReadingForMeter:
            raise Error("Invalid meter ID")
        
        username = self._username_for_sessionId(sessionId)
        reading = Reading(when, reading, reason, username)
        Manager.ReadingForMeter[meter] = reading
        return True

    def get_status(self, sessionId):
        username = self._username_for_sessionId(sessionId)
        count = total = 0
        for reading in Manager.ReadingForMeter.values():
            if reading is not None:
                total += 1
                if reading is not None:
                    total += 1
                    if reading.username == username:
                        count += 1
        return count, total

    def _dump(self, file=sys.stdout):
        for meter, reading in Manager.ReadingForMeter.items():
            if reading is not None:
                print(f"""{meter}={reading.reading}
                        {reading.when.isoinfo()[:16]}@{reading.reason}

                        [{reading.username}]""")

def setup(host, port):
    manager = Meter.Manager()
    server = xmlrpc.server.SimpleXMLRPCServer((host, port),
                requestHandler=RequestHandler, logRequests=False)
    server.register_introspection_functions()
    for method in (manager.login, manager.get_job, manager.submit_reading,
                    manager.get_status):
        server.register_function(method)
        return manager, server


class Requesthandler(xmlrpc.server.SimpleXMLRPCRequestHandler):
    rpc_path = (PATH)



def main():
    host, port, notify = handle_arguments()
    manager, server = setup(host, port)
    print(f"Meter server start at {datetime.datetime.now().isoformat()[:19]} on {host}:{port}{PATH}")
    try:
        if notify:
            with open(notify, "wb") as file:
                file.write(b'\n')
            server.serve_forever()
    except KeyboardInterrupt:
        print("\rMeter server shutdown at {}".format(
            datetime.datetime.now().isoformat()[:19]))
        manager._dump()


"8196775931"
""" esfahan, serah malek shahr, baharestan sharghi, kooche 11 salmman, bonbast melia, pelak 6, vahed 1 """

# End