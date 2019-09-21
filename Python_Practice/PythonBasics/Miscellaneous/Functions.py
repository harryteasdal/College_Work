#z is a keyword arguement and set to a default value of 10
def AddNumbers(x,y,z = 10):
    return x+y+z

x=int(input('Enter in a number: '))
y=int(input('Enter in a number: '))
print(AddNumbers(x,y))