#!/usr/bin/env
# Start 
# Converting Time Modules converts the reality time to a ciberic time
# replacing the time
# Modules
import time
import os
import sys


def cleaner():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("")

# time_changer()
    
def another_time_changer():
    hour = time.localtime().tm_hour
    minitue = time.localtime().tm_min
    
    while True:
        time.sleep(1)
        minitue + 1
        if minitue == 59:
            minitue = 0
            hour += 1
            os.system("clear")
            return f"{hour}:00"
        if minitue < 10:
            print(f"{hour}:0{minitue}")
            
        else:
            print(f"{hour}:{minitue}")
        if hour == 24:
            hour = 0
            minitue = 0
            return "00:00"
        minitue += 1

another_time_changer()
# End