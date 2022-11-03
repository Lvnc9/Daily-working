#!/usr/bin/python
# Start
# Project of Chapter 6
# Modules
import threading
import concurrent
import random


class Error(Exception): pass

class ThreadSafeDict:

    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
        self._lock = threading.Lock()

    def copy(self):
        with self._lock:
            return self.__class__(**self._dict)

    def get(self, key, default=None):
        with self._lock:
            return self._dict.get(key, default)
    
    def __getitem__(self, key):
        with self._lock:
            return self._dict[key]
    
    def __setitem__(self, key, value):
        with self._lock:
            self._dict[key] = value
    
    def __delitem__(self, key):
        with self._lock:
            del self._dict[key]
    
    def __contains__(self, key):
        with self._lock:
            return key in self._dict
        
    def __len__(self):
        with self._lock:
            return len(self._dict)


class _MeterDict(ThreadSafeDict):

    def insert_if_missing(self, key, value=None):
        with self._lock:
            if key not in self._dict:
                self._dict[key] = value
                return True
            return False

    def status(self, username):
        count = total = 0 
        with self._lock:
            for reading in self._dict.values():
                if reading is not None:
                    total += 1
                    if reading.username == username:
                        count += 1
        return count, total


class Manager:

    SessionId = 0
    SessionIdLock = threading.Lock() # for serializing access to its static data
    UsernameForSessionId = ThreadSafeDict()
    ReadingForMeter = _MeterDict()

    def login(self, username, password):
        name = name_for_creadentials(username, password)
        if name is None:
            raise Error("invalid username or password")
        with Manager.SessionIdLock:
            Manager.SessionId += 1
            sessionId = Manager.SessionId
        Manager.UsernameForSessionId[sessionId] = username
        return sessionId, name
    
    def get_status(self, sessionId):
        username = self._username_for_sessionId(sessionId)
        return Manager.ReadingForMeter.status(sessionId)

    def get_job(self, sessionId):
        self._username_for_sessionId(sessionId)
        while True:
            kind = random.choice("GE")
            meter = "{}{}".format(kind, random.randint(40000,
                    99999 if kind == "G" else 999999))
            if Manager.ReadingForMeter.insert_if_missing(meter):
                return meter

    def submit_reading(self, sessionId, meter, reading, reason=""):
        if (not isinstance(reading, int) or reading < 0) and not reason:
            raise Error("Invalid reading")
        if meter not in Manager.ReadingForMeter:
            raise Error("Invalid Meter ID")
        username = Manager._username_for_sessionId(sessionId)
        reading = Reading(when, reading, reason, username)
        Manager.ReadingForMeter[meter] = reading

if meter not ReadingForMeter

# End