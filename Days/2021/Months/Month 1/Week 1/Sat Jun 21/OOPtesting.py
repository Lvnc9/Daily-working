#! python3
# Start
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

# Ussing some a new method names super()
class Friend(Contact):
    def __init__(self, name, email, phone):
        self.phone = phone
        super().__init__(name, email)

# Use a bit of mixin 
class EmailResponder:
    def checker(self):
        return [True if self.EmailCompaler else print('Email does not exist yet!')]

    def message_sender(self, message:str):
        if self.email:
            return self.email + ('\nMessage:->\t' + message)
        else:
            print('pleas enter your email address')

class EmailCompaler(Contact, EmailResponder):
        pass

class AddressHolder:
    "Give 4 inputs for makng a full address data"
    def __init__(self, city, streat, state, code):
        self.city = city
        self.streat = streat
        self.state = state
        self.code = code

class Friend(Contact):
    "Container of the users info"
    
    def __init__(self, name:str, email:str, phone:str, address:str):
        self.address = AddressHolder('Kanzes', '5321 hd pashla', 'CA', '10020')
        self.phone = phone
        super().__init__(name, email)

    if __init__:
        print('Saved')

f1 = Friend('Pashmak', 'sam.mohammadi2154@gmail.com', '243-432-4324'', )
# End