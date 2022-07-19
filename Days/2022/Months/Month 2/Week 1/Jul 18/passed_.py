#! python3.10.4
# Start
# Working on saving data as bytes and making them movealbe to multisystems
# Modules
import pickle


some_data = ['idk somwhere else',
            'you will find it out',
            'so be to much True',
            'cause im lost in space',
            'dont know where is my home',
            'how sad that can be',
            'how sad that could be',
            'to be away from your home',
            'dont have a place to go',
            'yea that is to sad',
            'yea tell me something',
            'how could i find my way back',
            'to the place i left out!']

with open('a list', 'wb') as file:
    pickle.dump(some_data, file)

with open('a list', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data, 'loaded data is not loaded'

""" application gozine poshte paiin 
paiam : sms 
tamas : na
 """
# End