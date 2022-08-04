#!/usr/bin/python
# Start
# Modules
from UI import UserInterface


# Runer
def run():
    runer_instance = UserInterface()
    runer_instance.shower()
    runer_instance.loading()
    runer_instance.file_cheker()
    runer_instance.loading()
    runer_instance.xfs_finder()


if __name__ == "__main__":
    run()


# End