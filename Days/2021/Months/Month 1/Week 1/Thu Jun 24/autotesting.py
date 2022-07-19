#! python3 
# Start
# Modules
import os, send2trash, shutil, numpy as np, shelve

# The most importent funcion
def clear():
    os.system('clear')


first_array = np.array([[1, 10, 15], [20, 25, 30], [35, 40, 45]], ndmin=3, dtype=np.uint32)
secend_array = np.array([[50, 55, 60], [65, 70, 75], [80, 85, 90]], ndmin=3, dtype=np.uint32)


for number in np.nditer(first_array, flags=['buffered'], op_dtypes=['S']):
    print(number)

for indx, number in np.nditer(first_array, secend_array):
    print(indx, number)
# End