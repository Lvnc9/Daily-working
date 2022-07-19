#! python3.10.4
# Start
# Sequental unpackingg and etc.
# Modules
import os

args = (600, 900)
kwargs = dict(copies=2, collate=False)

def print_setup(width, height, copies=None, collate=None):
    print(width, height, copies, collate)
    print(f'This is height {height}')


# How to unpack values to the function with the lowest energy
print_setup(*args, **kwargs)

# you can put tuple and dict to the functions 
def print_args(*args, **kwargs):
    print(args.__class__.__name__, args,
        kwargs.__class__.__name__, kwargs)
    
os.system("clear")
print_args()
print_args(1, 2, 3, a=1)


# End