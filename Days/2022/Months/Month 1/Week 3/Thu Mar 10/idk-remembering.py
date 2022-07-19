#! python3.9.9
# Start
# Modules
from collections import namedtuple, defaultdict
from functools import total_ordering
from queue import Queue

test_pashmak = Queue(maxsize=2)
test_pashmak.put('you', block=False, timeout=2)
test_pashmak.put('yes you', block=False, timeout=2)
test_pashmak.put('how long', timeout=2)



# End