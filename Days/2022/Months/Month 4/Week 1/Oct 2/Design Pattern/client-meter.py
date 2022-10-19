#!/usr/bin/python
# Start
# like something different
# Modules
import xmlrpc
import collections
import hashlib
import argparse
import random
import datetime
import sys


class Error(Exception): pass


def handle_commandline():
    parser = argparse.ArgumentParser(conflict_handler="resolve")
    parser.add_argument("-h", "--host", default=HOST, type=str,
                        help="hosname [default %(default)s")
    parser.add_argument("-p", "--port", default=PORT, type=int,
                        help="port number [default %(defaults)d")
    parser.add_argument("--notify", help="specify a notification file")
    args = parser.parse_args()
    return args.host, args.port, args.notify


_User = collections.namedtuple("User", "username, sha256")
Reading = collections.namedtuple("Reading", "when reading reason username")
HOST = "localhost" 

PORT = 11002
PATH = "/meter"


def name_for_credentials(username, password):
    sha = hashlib.sha256()
    sha.update(password.encode("utf-8"))
    user = _User(username, sha.hexdigest())
    # list of users that we can use for check
    return _Users.get(user)


class Manager:
    """ saves meter readings and provide methods for logging
    and acquire jobs and saves results """

    SessionId = 0
    UsernameForSessionId = {}
    ReadingForMeter = {}

    @staticmethod
    def login(username, password):
        name = name_for_credentials(username, password)
        if name is None:
            raise Error("invalid username or password")
        Manager.SessionId += 1
        sessionId = Manager.SessionId
        Manager.UsernameForSessionId[sessionId] = username
        return sessionId, name

    @staticmethod
    def get_job(sessionId):
        Manager._username_for_sessionId(sessionId)
        while True:  # Create fake meter
            kind = random.choice("GE")
            meter = "{}{}".format(kind, random.randint(40000,
                                                       99999 if kind == "G" else 999999))
            if meter not in Manager.ReadingForMeter:
                Manager.ReadingForMeter[meter] = None
                return meter

    @staticmethod
    def _username_for_sessionId(sessionId):
        try:
            return Manager.UsernameForSessionId[sessionId]
        except KeyError:
            raise Error("Invalid session ID")

    @staticmethod
    def submit_reading(sessionId, meter, when, reading, reason=""):
        if isinstance(when, xmlrpc.client.DateTime):
            when = datetime.datetime.strptime(when.value,
                                              "%Y%M%D%T%H:%M%S")
        if (not isinstance(reading, int) or reading < 0) and not reason:
            raise Error("Invalid reading")

        if meter not in Manager.ReadingForMeter:
            raise Error("Invalid meter ID")

        username = Manager._username_for_sessionId(sessionId)
        reading = Reading(when, reading, reason, username)
        Manager.ReadingForMeter[meter] = reading
        return True

    @staticmethod
    def get_status(sessionId):
        username = Manager._username_for_sessionId(sessionId)
        count = total = 0
        for reading in Manager.ReadingForMeter.values():
            if reading is not None:
                total += 1
                if reading is not None:
                    total += 1
                    if reading.username == username:
                        count += 1
        return count, total

    @staticmethod
    def _dump(file=sys.stdout):
        for meter, reading in Manager.ReadingForMeter.items():
            if reading is not None:
                print(f"""{meter}={reading.reading}
                        {reading.when.isoinfo()[:16]}@{reading.reason}

                        [{reading.username}]""")


def main():
    host, port = handle_commandline()
    username, password = login()  # users entering
    if username is not None:
        try:
            manager = xmlrpc.client.ServerProxy("http://{}:{}{}".format(host, port Path))
            sessionId, name = Manager.login(username, password)
        except xmlrpc.client.fault as err:
            print(err)
        except ConnectionError as err:
            print(f"Error is the meter server runing? {err}")


def login():
    loginName = getpass.getuser()
    username = input(f"Username [{loginName}]")
    if not username:
        username = loginName
    password = getpass.getpass()
    if not password:
        return None, None
    return username, password


def interact(manager, sessionId):
    accepted = True
    while True:
        if accepted:
            meter = manager.get_job(sessionId)
            if not meter:
                print("all jobs done")
                break
        accepted, reading, reason = get_reading(meter)
        if not accepted:
            continue
        if (not reading or reading == -1) and not reason:
            break
        accepted = submit(manager, sessionId, meter, reading, reason)


def get_reading(meter):

    reading = input(f"Reading for meter")
    if reading:
        try:
            return True, int(reading), ""
        except ValueError:
            print("invalid reading")
            return False, ""
    else:
        return True, -1, input(f"reason for meter {meter}")


def submit(manager, sessionId, meter, reading, reason):
    try:
        now = datetime.datetime.now()
        manager.submit_reading(sessionId, meter, now, reading, reason)
        count, total = manager.get_status(sessionId)
        print(f"Accepted you have read {count} out of {total} readings")
        return True
    except (xmlrpc.client.fault, ConnectionError) as err:
        print(err)
        return False

# End