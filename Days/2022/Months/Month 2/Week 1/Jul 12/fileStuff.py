#! python3.10.4
# Start
# working with bytes and strings
# Moduels
import sys


def filepasser():
    """ create the name file and text for
    naming teh file and perparing the text for adding 
    to them """

    txt = input("What you wanna say?\n")
    filename = input("What is the name file?\n")

    return (txt, filename)

txt, filename = filepasser()

with open(filename, 'w') as file:
    file.write(txt)
with open(filename, 'r') as file:
    doc = file.read()


if __name__ == "__main__":
    filepasser()
    print(doc)


# End