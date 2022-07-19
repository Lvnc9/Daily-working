#! python3.9.9
# Start
# Collect all the links in the website and stop the app to loop on the links that are passing in :)
# Modules
from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
from functools import total_ordering

from parso import parse

# Part 1
LINK_REGEX = re.compile(
    "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

@total_ordering
class LinkCollector:
    """ Collect all the links and the sub linkes of
    links  """

    def __init__(self, url:str):
        self.url = "" + urlparse(url).netloc
    
    def collect_links(self, path="/"):
        full_url = self.url + path
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        print(links)


if __name__ == "__main__":
    LinkCollector(sys.argv[1]).collect_links()


# End