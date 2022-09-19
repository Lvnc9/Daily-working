#!/usr/bin/python
# Start
# Threading 
# Moudles
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import os
import tempfile
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

def process(futures):
    canceled = False
    done = 0
    filename = os.path.join(tempfile.tempdir(), "whatsnew.html")
    with open(filename, "wt", encoding="utf-8") as file:
        file.write("<!doctype html>\n")
        file.write("<html><head><title>What's New</title></head>\n")
        file.write("<body><h1>What's new</body></h1>\n")
        canceled, results = wait_for(futures)
        if not canceled:
            for result in (result for ok, result in results if ok
                            and result is not None):
                done += 1
                for item in result:
                    file.write(item)


# End