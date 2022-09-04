#!/usr/bin/python
# Start
# I/O bound operations
# Modules
import multiprocessing 
import threading
import Feed
import queue
import os
import Qtrac
import argparse


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit" type=int, default=0,
                        help="the maximum item per feed [default: unlimited]")
        
    parser.add_argument("-c", "--concurrency", type=int,
                        default=multiprocessing.cpu_count() * 4,
                        help="specify the currency (for debugging and "
                        "timing [default: %(default)d]")
    args = parser.parse_args()
    return args.limit, args.concurrency


def create_threads(limit, jobs, results, concurrency):
    for _ in range(concurrency):
        thread = threading.Thread(target=worker, args=(
            limit, jobs, results))
    thread.daemon = True
    thread.start()


def worker(limit, jobs, results):
    while True:
        try:
            feed = jobs.get()
            ok, result = Feed.read(feed, limit)
            if not ok:
                Qtrac.report(result, True)
            elif result is not None:
                Qtrac.report(f"read {result[0][0:46]}")
                results.put(result)
        finally:
            jobs.task_done()
    



# Where code gathers
def main():
    limit, concurrency = handle_commandline()
    Qtrac.report("Starting...")
    filename = os.path.join(os.path.dirname(__file__), "whatnew.dat")
    jobs = queue.Queue()
    results = queue.Queue()
    create_threads(limit, jobs, results, concurrency)
    todo = add_jobs(filename, jobs)
    process(todo, jobs, results, concurrency)



if __name__ == "__main__":
    main()
# End