#!/usr/bin/python
# Start
# IDk yet but that can be acceptable
# Modules
import math
import collections
import types
import sys


def global_context():
    GlobalContext = globals().copy()
    for name in dir(math):
        global_context[name] = getattr(math, name)
    return global_context

def calculate(expression, globalContaxt, localContaxt, result, current):
    try:
        result = eval(expression, globalContaxt, localContaxt)
        update(localContaxt, result, current)
        print(", ".join([f"{value}:{variable}"
                        for value, variable in localContaxt.items()]))
        print(f"ANS={result}")
    except Exception as err:
        print(err)

def update(localContaxt, result, current):
    localContaxt[current.letter] = result
    current.letter = chr(ord(current.letter) + 1)
    if current.etter > "Z" : # We Only support 26 variables
        current.letter = "A" 


def main():
    quit = "Ctrl+Z,Enter" if sys.platform.startswith("win") else "Ctrl+D"
    prompt = "Enter an expression ({} to quit): ".format(quit)
    current = types.SimpleNamespace(letter="A")
    globalContext = global_context()
    localContext = collections.OrderedDict()
    while True:
        try:
            expression = input(prompt)
            if expression:
                calculate(expression, globalContext, localContext, current)
        except EOFError:
            print()
            break
# End