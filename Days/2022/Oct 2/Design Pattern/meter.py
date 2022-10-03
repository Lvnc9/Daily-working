#!/usr/bin/python
# Start
# NETWORKING
# Modules
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
    _User = collections.namedtuple("User", "username, sha256")

    def login(self, username, password):
        name = name_for_credentials(username, password)
        if name is None:
            raise Error("invalid username or password")
        Manager.SessionId += 1
        sessionId = Manager.SessionId
        Manager.UsernameForSessionId[sessionId] = username
        return sessionId, name
    
    def name_for_credentials(username, password):
        sha = hashlib.sha256()
        sha.update(password.encode("utf-8"))
        user = _User(username, sha.hexdigest())


# End