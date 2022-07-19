#! python3.9.2
# Start
# Purpose : repeating all the codes and structures for practice
# TODO: Modules # NOT EXIST YET :I
# Exceptions
class NotAvailableFileFormat(Exception):
    print('')

class AudioFile(object):
    def __init__(self, filename:str):
        if not filename.startswith(self.ext):
            raise NotAvailableFileFormat("Error: File Format isn't Available")

        self.filename = filename

class Mp3(AudioFile):
    """ Extend Audiofile parent class
    recognize the mp3 files and plays them """
    ext = "Mp3"

    def playing(self):
        print(f"Playing {self.ext} songs")

class Flac(AudioFile):
    """ Extending the Audiofile Parent class
    recognize the flac audios and plays them """

    ext = "Flac"

        
# End