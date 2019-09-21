def Factorial(n):
    #this is the base case that takes the program out of the  recursive loop
    if n ==1 or n==0:
        return 1
    else:
        #this is the recursive case and makes the function recursive 
        return n*(Factorial(n-1))

n =int(input("Enter a number: "))
print(Factorial(n))