#!/usr/bin/python
# Start
# reading from url 
# Modules
from html import escape
import urllib
import socket
import feedparser

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

def _parse(data, limit):
    output = []
    feed = feedparser.parse(data) # Atom + RSS
    for entry in feed["entries"]:
        title = entry.get("title")
        link = entry.get("link")
        if title:
            if link:
                output.append('<li><a href="{}">{}</a></li>'.format(
                            link, escape(title)))
            else:
                output.append('<li>{}</li>'.format(escape(title)))
        if limit and len(output) == limit:
            break
    if output:
        return ["<ul>"] + output + ["</ul>"]
# End