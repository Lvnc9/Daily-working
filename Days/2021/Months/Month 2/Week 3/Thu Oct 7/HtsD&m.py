#! python3.9.2
# Start
### Working on the old codes and training in them to remember how to code like past ;)
# this is a bad situation, but cant do anything about it l|###
# TODO: Modules

class Contact(object):
    all_contacts = []

    def __init__(self, name:str='', fname:str='', 
    **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.fname = fname
        self.all_contacts.append(self)

class AdressHolder(object):
    def __init__(self, streat='', city='', state='',
    code='', **kwargs):
        super().__init__(**kwargs)
        
# End