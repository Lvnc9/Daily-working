#! python3 
# Start
# Modules
import os 
import abc


class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
print(s.num_base_calls)

class BaseClass:
    "plays as the object class exmpale in this prototype"
    
    num_base_calls = 0
    def call_me(self):
        print('Calling the base Class')
        self.num_base_calls

class LeftClass(BaseClass):
    "Secend player of the diamond problom in OOP"
    
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print('Calling left class')
        self.num_left_calls += 1

class RightClass(BaseClass):
    "Third player of the diamond problom in OOP"

    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print('calling the right Class')
        self.num_right_calls += 1
LeftClass, RightClass
class SubClass(RightClass, LeftClass):
    "Play as the Fourth player of the diamond problom"

    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print('calling the sub class')
        self.num_sub_calls += 1

os.system('clear')
pashmak_obj = SubClass()
pashmak_obj.call_me()
# End