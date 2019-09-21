#this is the function that calculates the probability of one of two player winning. 
def Probability(Rating1,Rating2,Player): 
    if Player == 1:
         #this is the elo equation and calculates the probability of player A winning
         #the probability is a number between 0 and 1 
        Expected_Outcome= 1/(1+10**((Rating2-Rating1)/400))
        #returns the answer multiplied by 100 to represent it as a percentage 
        return Expected_Outcome*100
    elif Player == 2:
        #this is the elo equation that calculates the probability of player B winning1
        Expected_Outcome= 1/(1+10**((Rating1-Rating2)/400)) 
        return Expected_Outcome*100
    else:
        #Displays error message when somthing other than A or B is entered 
        print("Sorry,that isnt one of the players.")

rating1 = int(input("Enter in player 1 rating: "))
rating2 = int(input("Enter in player 2 rating: "))
player = int(input("Which player do you want the probability for (1 or 2): "))
print(str(round(Probability(rating1,rating2,player)))+'%')