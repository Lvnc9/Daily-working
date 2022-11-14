#!/usr/bin/venv
# Start
# training old design patterns
# Modules


class SingletonObj:
    class __SingletonObj:
        number = 1
        def __init__(self, filename=""):
            self.filename = filename

        def shower(self):
            with open(filename, 'w') as lala:
                lala.write(f"something interesting happend\ntries:{number}") 
                SingletonObj.__SingletonObj.number += 1
    instance = None
        





# End