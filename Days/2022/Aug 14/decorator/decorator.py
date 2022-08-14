#!/usr/bin/python
# Start
# IDK SOMETHING YOU CAN SAY THAY DOES WORK
# Modules
import time
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = time.time()
        print(f"calling {func.__name__} with {args} and {kwargs}")
        return_value = func(*args, **kwargs)
        print(F"Ececuting {func.__name__} at {time.time() - now}")
        return return_value
    return wrapper

@log_calls
def test1(a,b,c):
    print("\ttest1 called")

@log_calls
def test2(a,b):
    print("\ttest2 called")

@log_calls
def test3(a,b):
    print("\ttest3 called")
    time.sleep(1)

# if we dont use the @decorator syntax
test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1,2, 3)
test2(4,b=5)
test3(6,7)

# End