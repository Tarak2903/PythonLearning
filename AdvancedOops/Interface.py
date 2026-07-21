from abc import ABC,abstractmethod


class Pay(ABC):
    @abstractmethod
    def pay(self):
        pass

class B(Pay):
    def pay(self):
        print("I am implenting this mehotf herer")

x=B()