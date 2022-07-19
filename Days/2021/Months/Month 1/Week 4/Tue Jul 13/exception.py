#! python3
# Start
# Will disccuss more about the Exceptions xd


class InvalidWithdraw(Exception):
    """Exception : Error
    occure when the balance money is not enough 
    for the amount user about to buy :)"""

    def __init__(self, amount:int, balance:int):
        super().__init__(f"Account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance
    
    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdraw(30, 125)

except InvalidWithdraw as exc:
    print(f"Im sorry but your balance is lesser than your amount! {exc.overage()}")
    
# End