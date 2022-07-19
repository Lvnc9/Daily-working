#!python3.10.4
# Start
# Entering to I/O Field HMM :)
# Modules
import os
import random, string

import urllib3

class Pashmak:
    """ not now """

    def __str__(self):
        return "I am pashmak"

    def __repr__(self):
        return 'you are pashmamk'
    

lilone = Pashmak()
print(lilone)
print(f"Pashmak{Pashmak}")


class StringJoiner(list):
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.result = " ".join(self)


with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(string.ascii_letters)

print(joiner.result)

class Pashmaker:
    """ bullshit playing with overload methods """


    def pashmak(self, pp=[]):
        return pp

#def __str__(self):
#    return self.pashmak


lala = Pashmaker()
lala.pashmak([1, 2])
print(lala.pashmak())

def linker(*links):
    for link in links:
        if "linux" in os.system("uname -a".lower()):
            os.system("httrack link")
        else:
            urllib3.connection_from_url(link)
        print(f"Link {link} -> has been downloaded")

linker("")
# End