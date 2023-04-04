from abc import ABC,abstractmethod

class Car(AvBC):
    def milage(self):
        pass

class Tesala(Car):
    def milage(self):
        print("yess 50")

class TATA(ABC):
    def milage(self):
        print("80")

t1=TATA()
t1.milage()
t1=Tesala()
t1.milage()