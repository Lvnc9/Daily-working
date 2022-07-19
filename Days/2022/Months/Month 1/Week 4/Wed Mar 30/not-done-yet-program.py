#!python3.9.9
# Start
# End of the chapter 5
# Modules
from os import link
from urllib.request import urlopen
from urllib.parse import urlparse
import re
from sys import argv

# The base algorithm for finding the desired links in the server 
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
        self.url = "http://" + urlparse(url).netloc
        self.collected_links = set()
        self.visited_links = set()

    def collect_links(self, path="/"):
        full_url = self.url + path
        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)

        #New Code Arrives for new collected Links
        links = {self.normalize_url(path, link
        ) for link in links}
        self.collected_links = links.union(
            self.collected_links)
        unvisited_links = links.difference(
            self.visited_links)

        print(links, self.visited_links, 
        self.collected_links, unvisited_links)

    def normalize_url(self, path:str, link:str):
        if link.startswith("http://"):
            return link
        elif link.startswith("/"):
            return self.url + link
        else:
            return self.url + path.rpartition(
                '/')[0] + '/' + link

if __name__ == "__main__":
    LinkCollector(argv[1]).collect_links()

# End