#!/usr/bin/python
# Start
# Flight Status app that sets them and looks for them in key value pairs
# its not usefull to write a test for checking the database to make sure 
# it is placed instead we have to use Mock object
# Modules
import datetime
import redis


class FlightStatusTracker:
    
    ALOWED_STATUSES = {'CANCELED', 'DELAYED', 'ON TIME'}

    def __init__(self):
        self.redis = redis.StrictRedis()
    
    def change_status(self, flight, status):
        status = status.upper()
        if status not in FlightStatusTracker.ALOWED_STATUSES:
            raise ValueError(f"{status} is not a valid status")
        key = f"flightno : {flight}"
        value = f"{datetime.datetime.isoformat} {status}"
        self.redis.set(key, value)
    


# End