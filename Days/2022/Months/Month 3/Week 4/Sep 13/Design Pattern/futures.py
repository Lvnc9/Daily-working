#!/usr/bin/python
# Start
# Threading 
# Moudles
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import tempfile
import webbrowser
import Qtrac


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", type=int, default=0,
                        help="the maximum item per feed [default: unlimited]")
        
    parser.add_argument("-c", "--concurrency", type=int,
                        default=multiprocessing.cpu_count() * 4,
                        help="specify the currency (for debugging and "
                        "timing [default: %(default)d]")
    args = parser.parse_args()
    return args.limit, args.concurrency


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
        done, filename, canceled = process(futures)
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
        else:
            done = sum(1 for ok, result in results if ok and 
                        result is not None)
        file.write("</body></html>\n")
    return done, filename, canceled


def wait_for(futures):
    canceled = False
    results = []
    try:
        for future in as_completed(futures):
            err = future.exception()
            if err is None:
                ok, result = future.result()
                if not ok:
                    Qtrac.report("read {}".format(result[0][4:-6]))
                results.append((ok, result))
            else:
                raise err # Unanticipated
    except KeyboardInterrupt():
        Qtrac.report("canceliing...")
        canceled = True
        for future in futures:
            future.cancel()
    return canceled, results

# End