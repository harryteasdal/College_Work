#computer can actually assign infinity so assigns a really big number
from sys import maxsize
##TREE BUILDER
class Node(object):
    def __init_(self,i_depth,i_playerNum,i_sticksRemaining,i_value=0):
        #depth into the tree
        self.i_depth = i_depth
        #player number either 1 or -1 
        self.i_playerNum=i_playerNum
        self.i_sticksRemaining = i_sticksRemaining
        #The value of each node 
        self.i_value=i_value
        #children is an empty list 
        self.children = []
        #calls function that creates children function
        self.CreateChildren()
    
    def CreateChildren(self):
        #checks to see if we have passed depth 0 (Base case)
        if self.i_depth >=0:
            for i in range(1,3):
                #how many sticks remain
                v = self.i_sticksRemaining-i
                #Recursive case also calls RealVal Function 
                self.children.append(Node(self.i_depth-1,-self.i_playerNum,v,self.RealVal(v)))

    #detrmines if player has one ore overdrawn sticks
    def RealVal(self,value):
        if(value==0):
            return maxsize*self.i_playerNum
        elif(value<0):
            return maxsize*-self.i_playerNum
        return 0
        
##ALGORITHM
def MinMax(node,i_depth,i_playerNum):
    #checks to see id depth is zero or are we at a node at a win or lose condition
    if(i_depth==0)or(abs(node.i_value)==maxsize):
        #returns the value of that node (best choice) 
        return node.i_value
    #assigning infinity*opposite direction it wants to be -infinity for posisitive player
    i_bestValue = maxsize*-i_playerNum
    #iterates through all children and runs algorithm
    for i in range(len(node.children)):
        child =node.children[i]
        i_val=MinMax(child,i_depth-1,-i_playerNum)
 
        if(abs(maxsize*i_playerNum-i_val)<abs(maxsize*i_playerNum-i_bestValue)):
            i_bestValue=i_val
    return i_bestValue