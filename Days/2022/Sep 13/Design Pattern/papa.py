#!/usr/bin/python
# Start
# Threading 
# Moudles
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import os
import webbrowser



print(os.path.join(os.path.dirname(__file__), "whatsnew.dat"))

def main():
    limit, concurrency = handle_commandline()
    Qtrac.report("starting")
    filename = os.path.join(os.path.dirname(__file__), "whatsnew.dat")
    futures = set()
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        for feed in Feed.iter(filename):
            future = executor.submit(Feed.read, feed, limit)
            futures.add(future)
        done, filenmae, canceled = process(futures)
        if canceled:
            executor.shutdown()
    Qtrac.report("read {}/{} feeds using{} threads, {}".format(
        done, len(futures), concurrency, " [canceled]" if canceled else ""))

    print()
    if not canceled:
        webbrowser.open(filename)

# End