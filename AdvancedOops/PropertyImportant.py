class Bank:
    def __init__(self,balance):
        self._balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,val):
        self._balance=val

b=Bank(100)
b.balance+=20
print(b.balance)


