#! python3.10.4
# Start
# Working on a new chapter
# Modules
import datetime


orders = [('burger', 2, 5),
          ('fries', 3.5, 1),
          ('cola', 1.75, 3)]

print("PRODUCT  QUANTITY  PRICE  SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s}{1: ^9d}${2: <8.2f}${3: >5.2f}".format(
        product, quantity, price, subtotal))

print("{0:%Y-%m-%d %I:%M %p }".format(datetime.datetime.now()))
print(datetime.datetime.now())

characters = b'\x63\x6c\x69\x63\xe9'
print(characters.decode('latin1'))

# End
