class Board():
    def __init__(self):
        self.BoardWidth = None 
        self.BaordHeight = None 
        self.Board = [] 
    def Set_Dimensions(self,height,width):
        self.BaordHeight =height
        self.BoardWidth = width 
        self.Board = [self.BoardWidth,self.BaordHeight]
    