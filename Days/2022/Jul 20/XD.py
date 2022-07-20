#! python3.10.4
# Learning to user json and how to expend its abillities
# i.e. addding object __dict__ to json cause json hates objects \:###
# Modules
import json


class Contact:
    """ Basic contacts we wanna use later """

    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"



class ContactEncoder(json.JSONEncoder):
    """ Expanding JSONEncoder to take the attributes of

    from object and save them in the dictionary without anything
    extra  """
    
    @property
    def default(self, obj):
        """ First checks if the object is instance of the Contact 
        object and if its so it's __dict__ will be saved without anything
        extra """

        if isinstance(obj, Contact):
            return {'is_contact': True,
                    "first": obj.first,
                    "last": obj.last,
                    "full_name": obj.full_name}

        return super().default(obj)

def decode_contact(dic):
    """ back to black :| """
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic


c = Contact("John", "Smith")

### ContactEncoder is getting
# ###used to save object data without making nonesense code
lala1 = json.dumps(c, cls=ContactEncoder)

laka = json.loads(lala1, object_hook=decode_contact)
print(laka.first)

# End