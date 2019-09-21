class Circle():
    def __init__(self):
        self.radius = int(input('Enter in radius:'))
        self.diameter = self.radius*2
        
    def circumference(self,pi=3.141): 
        return self.diameter*pi
    def area(self,pi=3.141):
        return (pi*self.radius**2)

    
Circle = Circle()
Circle.Radius = int(input('Enter radius'))
print(Circle.area)
print(Circle.circumference)
