#! python3
# Start
# Working some pashmaki stuff with the old Exeptions
# Modules

class NotEnoughMoney(Exception):
    """Exception Class
    Occured only if bag is empty or not having enough money"""

    pass

try:
    raise NotEnoughMoney('Money In your bag is not enough!')
except Exception:
    print('Oops Something happend')

class InvalidWithdraw(Exception):
    """Excpetion Class:
    Get the current balance and a amount of money
    That the user wanted to withdraw"""

    def __init__(self, amount:int, balance:str):
        super().__init__(f"Account doesn't have the ${amount}")
        self.amount = amount
        self.balance = balance
    
    def overage(self):
        return self.amount - self.balance
#class InvalidWithdrawal(Exception):
#    def __init__(self, balance, amount):
#        super().__init__("account doesn't have ${}".format(
#            amount))
#        self.amount = amount
#        self.balance = balance
#    
#    def overage(self):
#        return self.amount - self.balance
#
#raise InvalidWithdrawal(25, 50)

try:
    raise InvalidWithdraw(10, 8)
except InvalidWithdraw as exc:
    print(f"""Sorry but your money is not enoght to buy the 
        thing you want
        you have ${exc.overage()} lesser""")
# End