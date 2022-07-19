#! python 3.2.9
# Start
# Deciding when to use objects and when to not use
# Modules
import time
from urllib.request import urlopen


class WebPage:
    """Using Property funcion to avoid repeating requests
    """

    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retriving new page...")
            self._content = urlopen(self.url).read()
        return self._content


webpage = WebPage("https://shecan.ir")
now = time.time()

content1 = webpage.content
print(time.time() - now)

time.sleep(2)
now = time.time()
content2 = webpage.content
print(time.time() - now)

print(content2 == content1)

class AverageList(list):
    """Using property to become presto on calculation
    of numbers of arrays, using property GF"""

    @property
    def average(self):
        return sum(self) / len(self)

lil = AverageList([1, 10, 15, 20])
print(lil.average)


# End