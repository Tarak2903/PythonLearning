from abc import ABC, abstractmethod

class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type=='UPI':
            return UPI()
        elif payment_type=='CREDIT_CARD':
            return CreditCard()
        else:
            raise ValueError("Unknown payment type")




class Pay(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Pay):
    def pay(self):
        print("I am running on UPI")

class CreditCard(Pay):
    def pay(self):
        print("I am paying thu credit card")

class ShoppingCart:
    def __init__(self,payment):
        self.payment=payment
    def pay(self):
        self.payment.pay()


s1=ShoppingCart(PaymentFactory.create_payment('UPI'))
s1.pay()