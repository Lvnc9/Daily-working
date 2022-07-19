#! python3.9.9
# Start
# Modules
from urllib.request import urlopen
from urllib.parse import urlparse
import re
from sys import argv

# The base algorithm for finding thel living links in the server 
LINK_REGEX = re.compile(
    "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

# Linkfinder it self
class LinkCollector:
    """ idk how but have to try Man """
    """ it will init an url and save it it background,
    turn it into an abstrac path of address,
    download it,
    with regex that we defined in early will seperate links 
    from others,
    show an output """

    def __init__(self, url:str):
        self.url = "" + urlparse(url).netloc

    def collect_links(self, path="/"):
        full_url = self.url + path
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        print(links)


if __name__ == "__main__":
    LinkCollector(argv[1]).collect_links()


# End