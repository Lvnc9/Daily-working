#! python3.10.4
# Start
# Modules
import json


class Contact:
    """ Just normal attributes to add to json dicts """

    def __init__(self, last: str, first: str):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first}{self.last}"


class ContactEncoder(json.JSONEncoder):
    """ Reconfiguring JSONEncoder for encoding to
    dictionary -> if the parameter that is getting entered
    is Contact object we simply passing the old BS we saw earlier
    and just add it to the dictionary """

    def default(self, obj):
        if isinstance(obj, Contact):
            return {"is contact": True,
                    'first': obj.first,
                    'last': obj.last,
                    'full_name': obj.full_name}

        return super().default(obj)


c = Contact("pashmaker", "loloush")
print(json.dumps(c,  cls=ContactEncoder))
# End