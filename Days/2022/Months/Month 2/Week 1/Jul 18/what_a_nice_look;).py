#! python3.10.4
# Start
# Working on string and etc. module
# Modules
import sys
import re
import pickle


print(sys.getdefaultencoding())

b = bytearray(b'abcdef')
b[3] = ord(b'g')
b[4] = 68
print(b)


pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    print(f"'{search_string}' matches pattern '{pattern}'")
else:
    print(f"'{search_string}' doesn't matche pattern '{pattern}'")

pattern = "^[a-zA-Z]+@([a-z]+\.[a-z]+)$"
search_string = "pashmak@gmail.com"
match = re.match(pattern, search_string)

if match:
    print(match.group()[0])



# End