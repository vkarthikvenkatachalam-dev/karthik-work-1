# abstract
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class Cash (Payment):
    def make_payment(self, amount):
        print(f"Payment of ₹{amount} made on cash")

class Card(Payment):
    def make_payment(self, amount):
        print(f"Payment of ₹{amount} received using credit /debit card")