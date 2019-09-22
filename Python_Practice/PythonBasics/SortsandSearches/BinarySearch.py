original_dataset = [2,3,8,6,8]
search = int(input("Enter search: "))
flag = False 
i = 0 
while flag == False:
    if original_dataset[i] == search:
        flag = True 
        print(int("Item is in position: "+str(i))
    elif original_dataset[i] != search: 
        i = i +1 
        flag = False 
        