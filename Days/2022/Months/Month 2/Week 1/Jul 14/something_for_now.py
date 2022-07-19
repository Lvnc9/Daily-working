#! python3
# Start
# Working on methods and etc.
# Modules
import time
import datetime



class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay:float, callback):
        """ delay is parameter is in seconds """
        end_time = datetime.datetime.now() + \
            datetime.timedelta(seconds=delay)

        self.events.append(TimedEvent(end_time, callback))
    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)



# End