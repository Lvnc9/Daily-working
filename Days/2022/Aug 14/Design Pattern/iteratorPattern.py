#!/usr/bin/python
# Start
# Using iterator pattern for accecing data and files without exposing 
# to its collection or aggregate
# Module

# Implementing sequence protocol
class AtoZ:

    def __getitem__(self, index):
        if 0 <= index < 26:
            return chr(index + ord("A"))
        raise IndexError()

for item in AtoZ():
    print(item, end="")
print()


# End