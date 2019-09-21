#while(condition is true): do this
x = 0 
while x < 10:
    x+= 1
#set up multiple variables
x,y = 0,0 
while(True):
    x+= 1
    y+= 2
    if(x+y>10):
        #break stops the loop
        break
y = [1,2,3]
#for eache individual item within the range x
for i in y: 
    print(i)

for a in range(30):
    print(a)
#for i in range(min,max,step size)    
for i in range(10,30,2):
    print(i)

for i in range(30):
    if not(i%3):
        continue 
print(i)
