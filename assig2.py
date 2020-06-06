#Parent Class

class Customer:
    name = "luke"
    email = "luke@hotmail.com"
    phone = "1234567890"
    
    def getInfo(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter phone number: ")
        if(email == self.email and phone == self.phone):
            print("We will be with you!!")
        else:
            print("Try again")

#Creating the child
class User(Customer):
    name = 'Luke'
    email = "luke@hotmail.com"
    phone = "1234567890"
    def getInfo(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter phone number: ")
        if(email == self.email and phone == self.phone):
            print("We will be with you!!")
        else:
            print("Try again")

class payment(Customer):
    monthly_payment = 230
    id_number = '12345'
    def getInfo(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        id_number = input("Enter your id number: ")
        if(email == self.email and id_number == self.id_number):
            print("{}, We will be with you!!".format(name))
        else:
            print("Try again")
customer = User()
customer.getInfo()


Cars = payment()
Cars.getInfo()
