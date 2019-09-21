#inheritance-when on class gains the atrributes of another 
#inherits from object that allows inheritence tp happen 
class BaseClass(object):
    def printHam(self):
        print("Ham")

#the contents of the brackets are where it is inheriting from
class InheritingClass(BaseClass):
    pass
x = InheritingClass()
x.printHam()
 
 
