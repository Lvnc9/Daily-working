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
    
def another_time_changer(filename=None):
    try: 
        if not filename:
            hour = time.localtime().tm_hour
            minitue = time.localtime().tm_min
            wday = time.localtime().tm_wday
            month = time.localtime().tm_mon
            year = time.localtime().tm_year
            day = time.localtime().tm_mday
            while True:
                time.sleep(1)
                minitue + 1
                if minitue == 59:
                    minitue = 0
                    hour += 1
                    cleaner()
                    print("{hour}:00")
                if minitue < 10:
                    cleaner()
                    print(f"{hour}:0{minitue}") 
                if minitue >= 10:
                    cleaner()
                    print(f"{hour}:{minitue}")
                if hour == 24:
                    cleaner()
                    hour = 0
                    minitue = 0
                    print("00:00")
                    if wday == 6:
                        wday = 0
                        if day == 31:
                            day = 0
                            if month == 12:
                                month = 0
                                year += 1
                    day += 1
                    month += 1
                    wday += 1
                    minitue += 1
    except KeyboardInterrupt:
        with open("time.txt", "a") as file:
            file.write(year, " ", month,
                    " ", wday, " ", hour, " ", minitue)

another_time_changer()
# End