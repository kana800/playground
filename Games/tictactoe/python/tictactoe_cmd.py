import os
import itertools
#os.system("clear")

class Board:

    def __init__(self):
        self.cells = ["notaken"," "," "," "," "," "," "," "," "," "]

    def board_layout(self):
        print("-------")
        print("|%s|%s|%s|"%(self.cells[1],self.cells[2],self.cells[3]))
        print("-------")
        print("|%s|%s|%s|"%(self.cells[4],self.cells[5],self.cells[6]))
        print("-------")
        print("|%s|%s|%s|"%(self.cells[7],self.cells[8],self.cells[9]))
        print("-------")
    
    def update_board(self,player_no,player):
        if self.cells[player]==" ":
            if player_no == 1:
                self.cells[player] = "X"
            if player_no == 2:
                self.cells[player] = "O"
        
    def iswinner(self):
        setA = itertools.permutations([1,2,3])
        setB = itertools.permutations([4,5,6])
        setC = itertools.permutations([7,8,9])
        setD = itertools.permutations([1,5,9])
        setE = itertools.permutations([7,5,3])
        setF = itertools.permutations([1,4,7])
        setG = itertools.permutations([2,5,8])
        setH = itertools.permutations([3,6,9])
        
        for i in setA,setB,setC,setD,setE,setF,setG,setH:
            for k in list(i):
                if self.cells[k[0]] == self.cells[k[1]] == self.cells[k[2]] and self.cells[k[0]] != " ":
                    return True
    def isdraw(self):
        if " " in self.cells:
            return True
        return False

board = Board()
def refresh_screen(playerno,player):
    # refreshes our command line interface
    #os.system("clear")
    board.board_layout()
    board.update_board(playerno,player)
    board.iswinner()

board.board_layout()
while True:
    player1 = int(input("(X)>>INPUT A NUMBER BETWEEN 1-8: \n"))
    board.update_board(1,player1)
    board.board_layout()
    if board.isdraw() == False:
        print("Draw")
        break
    if board.iswinner() == True:
        print("Player 1 is winner")
        break

    player2 = int(input("(O)>>INPUT A NUMBER BETWEEN 1-8: \n"))
    board.update_board(2,player2)
    board.board_layout()
    if board.isdraw() == False:
        print("Draw")
        break
    if board.iswinner() == True:
        print("Player 2 is winner")
        break
     
