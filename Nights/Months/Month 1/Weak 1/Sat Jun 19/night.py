#! python3 
# Start
from contextlib import contextmanager
  
class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename
  
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()
  
# usage
message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as my_file:
    my_file.write('hello world')

# End