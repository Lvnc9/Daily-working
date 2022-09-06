#!/usr/bin/python
# Start
# reading from url 
# Modules
from html import escape
import urllib
import socket


def read(feed, limit, timeout=10):
    try:
        with urllib.request.urlopen(feed.url, None, timeout) as file:
            data = file.read()
        body = _parse(data, limit)
        if body:
            body =  [f"<h2>{escape(feed)}</h2>\n"] + body
            return True, body
        return True, None
    except (ValueError, urllib.error.HTTPError, urllib.error.URLError,
        socket.timeout) as err:
        return False, "Error: {}: {}".format(feed.url, err)


# End