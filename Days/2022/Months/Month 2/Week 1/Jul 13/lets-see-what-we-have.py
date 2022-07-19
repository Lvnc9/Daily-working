#! python3.10.4
# Start
# Working with OOP
""" Oh right pleas download this songs later : 
https://open.spotify.com/track/1NQM0YoTvX1s0i3N0aEBAN?si=6bff84752dd74ac2
 """
# Modules
import shutil 
import os.path
import datetime
import time



class Options:
    """ How to use kwargs in methods to make 
    overload methods and variable argumants :) """

    default_options = {
        'port' : 21,
        'host' : 'localhost',
        'username' : None,
        'password' : None,
        'debug' : False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)
    
    def __getattribute__(self, key):
        return self.options[key]

#options = Options(username='Sam', password='password', debug=True)


def augemented_move(target_folder, *filenames,
    verbose=False, **specific):
    """ Move all filename intor trget_folder, allowing
    specific treatment of certain files """

    def print_verbose(message:str, filename):
        """ prints the message if only verbose was
        enabled """
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose(verbose("ignoric {0}"), filename)
            elif specific[filename] == 'copy':
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)


class TimeEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback
    
    def ready(self):
        return self.endtime <= datetime.datetime.now()

class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        endtime = datetime.datetime.now() + \
            datetime.timedelta(seconds=delay)
            


# End