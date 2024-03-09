# printing game board
# taking player input
# check if user wins or ties
# switch the player
# check if win or tie again

import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X" # game starts with player X
winner_player = None # intialize with no value
game_running = True # game starts off

def printBoard(board):
    print(board[0] + " || " + board[1] + " || " + board[2])
    print("-----------")
    print(board[3] + " || " + board[4] + " || " + board[5])
    print("-----------")
    print(board[6] + " || " + board[7] + " || " + board[8])


def player_input(board):
    print(" ")
    pinput = int(input("Enter 1 to 9 to mark your territory: "))
    print(" ")
    if pinput >= 1 and pinput <= 9 and board[pinput - 1] == "-":
        board[pinput - 1] = current_player
    else:
        print("Womp Womp...already occupied!")
   
        
def board_horizontal(board):
    global winner_player
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner_player = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner_player = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        return True
   
    
def board_row(board):
    global winner_player
    if board[0] == board[3] == board[6] == board[0] != "-":
        winner_player = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner_player = board[2]
        return True 
 
    
def board_diag(board):
    global winner_player
    if board[0] == board[4] == board[6] and board[0] != "-":
        winner_player = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner_player = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner_player = board[2]
        return True     


def board_tie(board):
    global game_running
    if "-" not in board:
        printBoard(board)
        print("There's a tie!")
        game_running = False
        quit()
 
        
def different_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

        
def winner():
    if board_diag(board) or board_horizontal(board) or board_row(board):
        print("We have a winner: " + winner_player)
        quit()
        
def bot(board):
    while current_player == "O":
        index1 = random.randint(0,8)
        if board[index1] == "-":
            board[index1] = "O"
            different_player()              
        
while game_running:
    printBoard(board)
    player_input(board)
    winner()
    board_tie(board)
    different_player()
    bot(board)
    winner()
    board_tie(board)