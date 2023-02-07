import os    
import time    

board = [' ' for i in range(10)]    # initialize the board with empty spaces
player = 1    

# Constants for the state of the game
WIN = 1
DRAW = -1
RUNNING = 0
STOP = 1

# Start the game in a running state
game = RUNNING    
mark = 'X'    

# Draw the Tic-Tac-Toe game board
def draw_board():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    

# Check if a given position is empty
def check_position(position):    
    return board[position] == ' '

# Check if a player has won
def check_win():
    global game
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # vertical
        (1, 5, 9), (3, 5, 7)  # diagonal
    ]
    for win_condition in win_conditions:
        if all(board[i] != ' ' and board[i] == board[win_condition[0]] for i in win_condition):
            game = WIN
            return
    if all(board[i] != ' ' for i in range(1, 10)):
        game = DRAW

print("Tic-Tac-Toe Game Designed By Manan Patel")    
print("Player 1 [X] --- Player 2 [O]\n")    
print("Please Wait...")    
time.sleep(3)    
while(game == RUNNING):    
    os.system('cls')    
    draw_board()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        mark = 'X'    
    else:    
        print("Player 2's chance")    
        mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(check_position(choice)):    
        board[choice] = mark    
        player+=1    
        check_win()    

os.system('cls')    
draw_board()    
if(game == DRAW):    
    print("Game Draw")    
elif(game == WIN):    
    player-=1    
    if(player % 2 != 0):    
        print("Player 1 Won")    
    else:
        print("Player 2 Won")
