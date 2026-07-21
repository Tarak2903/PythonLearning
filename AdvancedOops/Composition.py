from abc import ABC,abstractmethod


class Engine(ABC):
    @abstractmethod
    def run(self):
        pass

class PetrolEngine(Engine):
    def run(self):
        print("I run on petrol")

class DieselEngine(Engine):
    def run(self):
        print("I am running on diesel")

class Car:
    def __init__(self,engine):
        self.engine=engine
    def run(self):
        self.engine.run()
        print("Car is running")

c=Car(DieselEngine())
c.run()
