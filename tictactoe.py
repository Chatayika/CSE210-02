import os
os.system("clear")

class Board():
    def__init__(self):
        self.cells = [" ", " " , " " , " ", " " , " ", " " , " ", " "]

    def display(self):
        print(self.cells[0],self.cells[1],(self.cells[2])
        print("---------------------------")
        print(self.cells[3],(self.cells[4],self.cells[5])
        print("---------------------------")
        print(self.cells[6],(self.cells[7],self.cells[8])
        

board = Board()
board.display()
