#! python3
# Start
# Will get some learning from the pashmaki thing Datetime library xd
# Moduels
import datetime
import threading
import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

#start_time = time.time()
#prod = calcProd()
#endtime = time.time()

#print(f"The result is {len(str(prod))} digits long.")
#print(f"Took {endtime - start_time} secends to calculate")


def shower(word:str):
    "Slow the argumant user entered"
    
    for i in word.upper():
        print(i, end='\t'), time.sleep(1)

shower('pashmak')



# End