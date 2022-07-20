#! python3.10.4
# Start
# Pickles best to save data that dont have time issue 
# Modules
from threading import Timer
import datetime
from urllib.request import urlopen


class UpdatedUrl:
    """ Downloading a web page every 3H and updating
    the data of them """
    def __init__(self, url:str):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.update = datetime.datetime.now()
        self.schedual()
    
    def schedual(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        """ removing timer from __dict__ of current object 
        pickle module can not pickle this, cause: self.timer
        pickle checks __getstate__ before __dict__ so we change it
        # and make object pickleable! """
        
        self.new_state = self.__dict__().copy()
        if 'timer' in self.new_state:
            del self.new_state['timer']
        return self.new_state

    def __setstate__(self, data):
        """ Taking infos from __getsate__ and add call the rmeoved
        method! """
        
        self.__dict__ = data
        self.schedual()
""" sdfsdafsdafsaf """



# End