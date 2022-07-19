#! python3.9.2
# Start
# reding the old parts of the book and repeating back all the things we knew and now we forgot
# TODO: MODULES

class Contact(object):
    """ One of the base parent class
    Moving information from the top to the bottom """

    def __init__(self, name:str, email:str, phone:int):
        self.name = name
        self.email = email
        self.phone = phone

class AddressHolder(object):
    """ One of the base parent class
    Moving information from the top to the bottom """

    def __init__(self, street:str, city:str, state:str, code:int):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friends(AddressHolder, Contact):
    pass



class BaseClass:
    num_base_calls = 0
    
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    
    def call_me(self):
        #super().call_me()
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        #super().call_me()
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        #super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

    
lil = Subclass()
lil.



# End