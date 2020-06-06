
#Creating a class

class number:
    def __init__(self):
        self._numberVar = 4
numb = number()
numb._numberVar = 54
print(numb._numberVar)

class number:
    def __init__(self):
        self.__privateVar = 24
        
    def getPrivate(self):
        print(self.__privateVar)
        
    def setPrivate(self, private):
        self.__privateVar = private
numb = number()
numb.getPrivate()
numb.setPrivate(67)
numb.getPrivate()
                    







if __name__ == "__main__":
    pass
