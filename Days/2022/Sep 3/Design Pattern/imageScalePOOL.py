#!/usr/bin/pyhthon
# Start
# Using Processpool except of multiprocessing 
# Modules
import concurrent
import os
import Qtrac
import collections


Summary = collections.namedtuple("Summary", "todo copied sclaed cancel")
def scale(size, smooth, source, target, concurrency):
    futures = set()
    with concurrent.futures.ProcessPoolExecutor(
            max_workers=concurrency) as executor:
        for sourceImage, targetImage in get_jobs(source, target):
            future = executor.submit(scale_one, size, smooth, sourceImage,
                targetImage)
            futures.add(future)
        summary = wait_for(futures)
        if summary.canceled:
            executor.shutdown()
        return summary

def get_jobs(source, target):
    for name in os.listdir(source):
        yield os.path.join(source, name), os.path.join(target, name)



def wait_for(futures):
    canceled = False
    copied = scaled = 0
    try:
        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                result = future.result()
                copied += result.copied
                scaled += result.scaled
                Qtrac.report("{} {}".format("copied" if result.copied else
                            "scaled", os.path.basename(result.name)))
            elif isinstance(err, Image.Error):
                Qtrac.report(str(err), True)
            else:
                raise err # Unanticipated
    except KeyboardInterrupt:
        Qtrac.report("canceling...")
        canceled = True
        for future in futures:
            future.cancel()
    return Summary(len(futures), copied, scaled, canceled)

# End