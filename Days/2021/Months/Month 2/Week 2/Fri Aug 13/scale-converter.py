#! python3.9.2
# Start
from .idk import ZipProcessor
import sys
from PIL import  Image

class ScaleZip(ZipProcessor):
    """ Continue of the ZipProcessor object load image
    files and Operates on them """

    def Process_files(self):
        """ Scale each Image in the direcotory to 640x480 """

        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(str(filename))

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
# End 