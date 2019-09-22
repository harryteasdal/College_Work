#a list is a data structure used for storing all data types 
x = ['banannas','apples',2,3.141]  
#to add to a list use ListName.append(what you want to add)
x.append('cheese')
#to insert a value use ListName.insert(Location,Value)
x.insert(2,'kiwi')
#to remove somthing use ListName.pop(location)
x.pop(2)
#to check the length of a list use len(ListName) it does not start at zero
print(len(x)) # the answer is 5 not 4 as it does not count from 0
#to convert an item to a list ise the list(item) function
print(list('Bread'))
print(x)