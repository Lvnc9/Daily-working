#!/usr/bin/python
# Start
# Multiprocessing for running different parts of programm and 
# probably sharing data between of them
# Modules
import sys

if sys.version_info < (3, 2):
    print("requires Python 3.2+ for concurrent.futures")
    sys.exit(1)

import argparse
import multiprocessing
import os
import collections
import Qtrac
import math


# this is a count of how many images have been copied how many have been scaled
Result = collections.namedtuple("Result", "copied scale name")
Summary = collections.namedtuple("Summary", "todo copied sclaed cancel")


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int,
                        default=multiprocessing.cpu_count(),
                        help="""(specifing the concurrency
                            for debugging and timing) [default: (default)d""")
    parser.add_argument("-s", "--size", default=400, type=int,
                        help="""make a scaled image that fits
                        the given dimension [default: %(default)d]""")
    
    parser.add_argument("-S", "--smooth", action="store_true",
                        help="use smooth scaling (slow but good for text)")
    
    parser.add_argument("source", help="""the directory containing the original
                         .xpm images""")

    parser.add_argument("target", help="the directory for the scaled .xpm images")
    
    args = parser.parse_args()
    source = os.path.abspath(args.source)
    target = os.path.abspath(args.source)
    if source == target:
        args.error("source and target most be different")
    if not os.path.exists(target):
        os.makedirs(target)
    return args.size, args.smooth, source, target, args.concurrency


def scale(size, smooth, source, target, concurrency):
    canceled = False
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(size, smooth, source, target, concurrency)
    todo = add_jobs(source, target, jobs)

    try:
    
        jobs.join()
    
    except KeyboardInterrupt: # MAY NOT WORK ON WINDOWS 
        Qtrac.report("canceling...")
    copied = scaled = 0 
    
    while not results.empty(): # SAFE BECAUSE ALL JOBS HAVE FINISHED
        result = results.get_nowait()
        copied += result.copied
        scaled += result.copied
    
    return Summary(todo, copied, scaled, canceled)


def create_processes(size, smooth, jobs, results, concurrency):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args=(
                                        size, smooth, jobs, results))
    process.daemon = True
    process.start()


def worker(size, smooth, jobs, results):
    # it is safe to use an INFINIT loop cause process is a deamon 
    # and will be terminated when programm has been finished
    while True:
        try:
            sourceImage, targetImage = jobs.get()
            try:
                result = scale_one(size, smooth, sourceImage, targetImage) #giving args to the actual function
                Qtrac.report(f"""{'copied' if result.copied else 'scale'} 
                {os.path.basename(result.name)}""")
                results.put(result)
            except Image.Error as err:  # Image Module not imported yet for not accesing to INTERNET!
                Qtrac.report(str(err), True)
        finally:
            jobs.task_done()


def add_jobs(source, target, jobs):
    for todo, name in enumerate(os.listdir(source), start=1):
        sourceImage = os.path.join(source, name)
        targetImage = os.path.join(target, name)
        jobs.put((sourceImage, targetImage))
    return todo


def scale_one(size, smooth, sourceImage, targetImage): #the main core 
    oldImage = Image.from_file(sourceImage)
    if oldImage.width <= size and oldImage.height <= size:
        oldImage.save(targetImage)
        return Result(1, 0, targetImage)
    else:
        if smooth:
            scale = min(size / oldImage.width, size / oldImage.height)
            newImage = oldImage.scale(scale)
        else:
            stride = int(math.ceil(max(oldImage.width / size,
                                    oldImage.height / size)))
            newImage = oldImage.subsample(stride)
        newImage.save(targetImage)
        return Result(0, 1, targetImage)


def summarize(summary, concurrency):
    message = f"copied {summary.copied} scaled {summary.scaled}"
    difference = summary.todo - (summary.copied + summary.scaled) 
    if difference:
        message += f"skipped {difference}"
    message += f"Using processes {concurrency}"
    if summary.canceld:
        message += " [canceled]"
    Qtrac.report(message)
    print()


def main():
    size, smooth, source, target, concurrency = handle_commandline()
    Qtrac.report("starting...")
    summary = scale(size, smooth, source, target ,concurrency)
    summarize(summary, concurrency)
    return summary

if __name__ == "__main__":
    main()

# End