import os
class Circle(object):
    def __init__ (self, radius):
        self.radius = radius
        self.diameter = self.radius*2
    def Circumference(self):
        return 3.141*self.diameter
    def Area(self):
        return 3.141*(self.radius**2)

hasWorked = False
os.system("cls")
while hasWorked == False:
    
 radius = int(input("Enter the radius: "))
 User_Circle = Circle(radius)
 Action = input("Do you want the Circumference (c) or the Area (a) ?: ") 
    
 if Action.lower() == "a":
      hasWorked = True
      print(User_Circle.Area())
 elif Action.lower() == "c":
     hasWorked == True
     print(User_Circle.Circumference())
 else:
     os.system("cls")
     print("Error Please Try Again")
     




 

