#! python3.9.9
# Start
# Talking about data structures and when n' how to use the
# Modules
from collections import KeysView, ValuesView, ItemsView

# Working with extended built ins
class SortedDict(dict):
    """ Is aboutt to store they keys in a sorted list 
    and show them with a methodcall """
    
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        """ Pahmak[test] = test2 Syntax """
    
        if not key in self.ordered_keys:
            self.ordered_keys.append(key)
    
        return super().__setitem__(key, value)
    
    def setdefault(self, key, value):
        if not key in self.ordered_keys:
            self.ordered_keys.append(key)
        
        return super().setdefault(key, value)

    def __iter__(self):
        """ for x in self Syntax """
        return self.ordered_keys.__iter__()

    def key(self):
        return KeysView(self)

    def value(self):
        return ValuesView(self)
    
    def items(self):
        return ItemsView(self)
    
# Testing its instantiation
talktalk = SortedDict()
talktalk['la la la'] = 'do you know'
talktalk['a'] = 'i know'
print(talktalk)

for pashmak in talktalk.items():
    print(pashmak)


# End