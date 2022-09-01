#!/usr/bin/python
# Start
# Writing log reporst from Queue and reporting them
# Modules
import sys


def report(message="", error=False):
    if len(message) >= 70 and not error:
        message = message[:67] + "..."
    sys.stdout.write(f"\r{message[:70]}{'\n' if error else '' }")
    # for prining it immeditatly
    sys.stdout.flush()


# End