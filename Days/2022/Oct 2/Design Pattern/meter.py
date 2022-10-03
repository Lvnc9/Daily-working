#!/usr/bin/python
# Start
# NETWORKING
# Modules
import random
import xmlrpc
import collections
import hashlib

class Error(Exception): pass

class Manager:
    """ saves meter readings and provide methods for logging
    and acquire jobs and saves results """

    SessionId = 0
    UsenameSeassionId = {}
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
            kind = random.choise("GE")
            meter = "{}{}".format(kind, random.randint(40000,
                    99999 if kind == "G" else  999999))
            if meter not in Manager.ReadingForMeter:
                Manager.ReadingForMeter[meter] = None
                return meter


_User = collections.namedtuple("User", "username, sha256")
    
def name_for_credentials(username, password):
    sha = hashlib.sha256()
    sha.update(password.encode("utf-8"))
    user = _User(username, sha.hexdigest())
    return _Users.get(user)



# End