#!/usr/bin/python
# Start
# VISITOR PATTERN applyis a funciton to items of a collection or aggeregation

lala = (21, 34, 53, 57, 967, 96)

def equality_adder(num):
    return '='.center(24) * num

pashmak = map(equality_adder, lala)

for item in pashmak:
    print(item)

# End