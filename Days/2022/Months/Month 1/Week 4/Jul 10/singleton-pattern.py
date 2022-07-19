#! python3.10.4
# Start
# Singleton pattern HooHooooo finally im going to kill this bastard ahhh
# Modules
import urllib
import re

# What we areeeeeeeeeee Doooooooooooooooooooooooooooooooooingggggggggggggggggggggggg

_URL = "http://www.bankofcanada.ca/stats/assets/csv/fx-seven-day.csv"


def get(refresh):
    """ Desined for singleton pattern, returns
    the value if it exists and wont let to add more """
    if refresh:
        get.rates = {}

    if get.rates:
        return get.rates
    with urllib.request.urlopen(_URL) as file:
        for line in file:
            line = line.rstrip().decode("urf-8")
            if not line or line.startwith(("#", "Date")):
                continue
            name, currency, *rest = re.split(r"\s*,\s*", line)
            key = f"{name} ({currency}"
            try : 
                get.rates[key] = float(rest[-1])
            except ValueError as err:
                print(f"error {err}: {line}")
        
    return get.rates

get.rates = {}
get("y")

# End