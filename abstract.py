from abc import ABC, abstractmethod
class rent(ABC):
    def paySlip(self, amount):
        print("Your rent payment amount: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass
class CardPayment(rent):
    def payment(self, amount):
        print('Your rent amount of {} is due. You have 3 days to pay your bill'.format(amount))
        obj = CardPaymemnt()
        obj.paySlip("$800")
        obj.payment("$200")





if __name__ == "__main__":
    pass
