#! python3
# Start
# Modules

# Using Polymorphism
class AudioFile:
    "Play the song and check the given format"

    def __init__(self, filename:str):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File format")

        self.filename = filename

class MP3player(AudioFile):
    "Play all the files with the extension mp3"

    ext = "mp3"
    def play(self):
        print(f"Playing {self.filename} as {self.ext}")
    
class WavFile(AudioFile):
    "Play all the files with the extension WavFile"

    ext = "wav"
    def play(self):
        print(f"Playing {self.filename} as {self.ext}")
    

class OggFile(AudioFile):
    "Play all the files with the extension "

    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))


class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename
    def play(self):
        print("playing {} as flac".format(self.filename))
``
# End