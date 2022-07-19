# Start
# Timer Playing
""" BULLSHIT!!!!!!!!
DOWNLOAD THIS LATER : https://open.spotify.com/track/370LALwO8rpzOeA8YaaS1g?si=e4d612acbd4340ee
 """
# Modules
from Jul14.something_for_now import Timer
import datetime


def format_time(message: str, *args):
    now = datetime.datetime.strftime("%I:%M:%S")
    print(message.format(*args, now=now))


def one(timer):
    format_time("{now} Called One")

def two(timer):
    format_time("{now} Called Two")

def three(timer):
    format_time("{now} Called Three")


class Repeater:
    def __init__(self):
        self.count = 0
    
    def repeater(self, timer):
        format_time("{now} repeat {0}", self.count)
        self.count += 1
        Timer.call_after(5, self.repeater)

    def __call__(self, timer):
        format_time("{now} repeat {0}", self.count)
        self.count += 1

        Timer.call_after(5, self)
timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, Repeater()138)
format_time("{now}: Starting")
timer.run()


# End
