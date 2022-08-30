#!/usr/bin/python
# Start
# using Mock object
# Modules
from unittest.mock import Mock
import py.test
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
    

def pytest_funcarg__tracker():
    return FlightStatusTracker()

def test_mock_method_(tracker):
    tracker.redis.set = Mock()
    with py.test.raises(ValueError) as ex:
        tracker.change_status("AC101", "lost")
    assert ex.value.args[0] == "LOST is not a valid status"
    assert tracker.redis.set.call_count == 0



# End