#Parent Class

class Customer:
    name = "luke"
    email = "luke@hotmail.com"
    phone = "1234567890"

class Cars:
    model = ['Ferrari','Ford','Lambo']
    Years = ['2017','2019','2020']

class User(Customer):
    name = 'Luke'
    email = "luke@hotmail.com"
    phone = "1234567890"

class payment(Cars):
    monthly_payment = 230
    name = 'Luke'
    def getInfo(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter phone number: ")
        if(email == self.email and number == self.number):
            print("We will be with you!!")
        else:
            print("Try again")
customer = User()
customer.getInfo()


cars = payment()
cars.getInfo()
