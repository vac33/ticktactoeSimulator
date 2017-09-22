import string
import sys

def printBoard():
    for i in range(3):
        for j in range(3):
            print(board[3*i+j], end = " ")
        print(" ")

def coordToIndex(coordStr):
    x = coordStr[0] 
    y = int(coordStr[1])-1 
    a = "ABC" 
    idx = a.index(x) 
    return (idx +3 *y)

def getPlay(isX):
    validInput = "ABC"
    validInput2 = "123"
    
    player = "X" if isX else "O"
    while(True):
        play = input("Player {}: ".format(player))
        if len(play) != 2:
            print("Not a valid move")
            continue           
        if play[0] not in validInput or play[1] not in validInput2:
            print("Not a valid move")
            continue
        idx = coordToIndex(play) 
        if board[idx] != " ":
            print("Already played")
            continue
        board[idx] = player 
        return idx 

def game():
    global board
    isXturn = True
    isValid = False
    
    while(True):
        getPlay(isXturn) 
        printBoard()
        winner = BoardInput()
        
        if winner == "X":
            print(winner + " has won!")
            
            while(isValid == False):
                getInput = input("Do you want to play again? Type 'Yes' or 'No': ")        
                if getInput == "yes" or getInput == "Yes" or getInput == "YES":
                    board = [" "]*9
                    return game()
                    isValid = True
                elif getInput == "no" or getInput == "No" or getInput == "NO":
                    board = [" "]*9
                    sys.exit()
                else:
                    print("Please type a valid string.")                  
        
        if winner == "O":
            print(winner + " has won!")

            while(isValid == False):
                getInput = input("Do you want to play again? Type 'Yes' or 'No': ")        
                if getInput == "yes" or getInput == "Yes" or getInput == "YES":
                    board = [" "]*9
                    return game()
                    isValid = True
                elif getInput == "no" or getInput == "No" or getInput == "NO":
                    board = [" "]*9
                    sys.exit()
                else:
                    print("Please type a valid string.")
                    
        if winner == "TIE":
            print("Game ends in a tie!")

            while(isValid == False):
                getInput = input("Do you want to play again? Type 'Yes' or 'No': ")        
                if getInput == "yes" or getInput == "Yes" or getInput == "YES":
                    board = [" "]*9
                    return game()
                    isValid = True
                elif getInput == "no" or getInput == "No" or getInput == "NO":
                    board = [" "]*9
                    sys.exit()
                else:
                    print("Please type a valid string.")
                                   
        isXturn = not(isXturn)
board = [" "]*9
        
def BoardInput():

    #Checks if X wins
    if board[0] + board[3] + board[6] == "XXX": 
        return "X"
    elif board[1] + board[4] + board[7] == "XXX":
        return "X"
    elif board[2] + board[5] + board[8] == "XXX":
        return "X"
    elif board[0] + board[4] + board[8] == "XXX":  
        return "X"
    elif board[2] + board[4] + board[6] == "XXX":
        return "X"
    elif board[0] + board[1] + board[2] == "XXX":
        return "X"
    elif board[3] + board[4] + board[5] == "XXX":
        return "X"
    elif board[6] + board[7] + board[8] == "XXX": 
        return "X"                                  

    #Checks if O wins
    elif board[0] + board[3] + board[6] == "OOO":
        return "O"
    elif board[1] + board[4] + board[7] == "OOO":
        return "O"
    elif board[2] + board[5] + board[8] == "OOO":
        return "O"
    elif board[0] + board[4] + board[8] == "OOO":
        return "O"
    elif board[2] + board[4] + board[6] == "OOO":
        return "O"
    elif board[0] + board[1] + board[2] == "OOO":
        return "O"
    elif board[3] + board[4] + board[5] == "OOO":
        return "O"
    elif board[6] + board[7] + board[8] == "OOO":
        return "O"

    #Checks if its a tie

    count = 0
    for i in "XO":
        for x in range(len(board)):
            if board[x] == i:
                count +=1
				
    if count == 9:
        return "TIE"
    

def gameTime(text):
    if text == "Y" or text == "y":
        game()
        
print("Welcome, to Tic Tac Toe.\nThis game requires coordinates.")
print("Valid coordinates are A-C and 1-3.\nAn example of the board can be found below:")
print("\tA1 B1 C1\n\tA2 B2 C2\n\tA3 B3 C3")
ready = input("Player X has the first turn. Press Y to play: ")
gameTime(ready)

    
