from abc import abstractmethod,ABC



class Pay(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Pay):
    def pay(self):
        print("I am paying by UPI")

class CreditCard(Pay):
    def pay(self):
        print("I am paying thru credit card")

class ShoppingCart:
    def __init__(self,payment_method):
        self.payment_method=payment_method
    def payment(self):
        self.payment_method.pay()

s1=ShoppingCart(CreditCard())
s2=ShoppingCart(UPI())

s1.payment()
s2.payment()
