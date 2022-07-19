#! python3
# Start
# Modules 
import os
import traceback

os.system('clear')
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Widthe must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An Exception Happend: ' + str(err))

        console = traceback.format_exc()
        os.system('clear')

print('do you want to see the traceback? y/n')
ans = input().lower()
if ans == 'y' or ans == 'yes' or ans == 'ye':
    print(console)


try:
    raise Exception("This is the error message.")
except:
    errorFile = open('ErrorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorinfo.txt.')

# End