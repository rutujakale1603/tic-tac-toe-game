import random


board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

# GAME BOARD

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8]) 


#take player input

def playerInput(board):
    inp = int(input("select a spot 1-9:"))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("oops player is already in that spot!")    


#check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] !="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] !="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] !="-":
        winner = board[6]
        return True
    

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !="-":
        winner = board[2]
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner = board[3]
        return True
    

def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] !="-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] !="-":
        winner = board[2]
        return True

def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"the winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"the winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"the winner is {winner}!")
        gameRunning = False    


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("it is a tie!")
        gameRunning = False
     
        
# switch the player
def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
       currentPlayer == "O"
    else:
        currentPlayer == "X"  

# computer 
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] == "O"
            switchplayer()


#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchplayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)

