#1 python3
# Start
import shelve
import datetime


class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
            "'{}' order to '{}'".format(order, self.name))


class LongNameDict(dict):
    "determine the longest key in dictionary"
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
print(longkeys.longest_key())

# End