# **************************************************************************
# Description: Tic Tac Toe Game
# Version: 1.1
# Author: CYoungX
# Date: 1/2/2020
# **************************************************************************

# *****************
# Global Functions
# *****************

# Function to print out a board for the game
from IPython.display import clear_output

def display_board(board):
    clear_output()

    print('\n  |   |  ')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--' +'\n  |   |  ')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--' +'\n  |   |  ')
    print(board[1]+' | '+board[2]+' | '+board[3])

# Function to take player input and assign marker as 'X' or 'O'
def player_input():

    marker = ''

    # KEEP ASKING PLAYER 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # ASSIGN PLAYER 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)

# Function to take in board list object, marker ('X' or 'O'), and the desired position (number 1-9) and assign it to the board.
def place_marker(board, marker, position):
     board[position] = marker

# Function that takes in a board and a mark (X or O), and then checks to see if that mark has won.
def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # Check Across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # Check Across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # Check Across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # Check the left from top down
    (board[8] == mark and board[5] == mark and board[2] == mark) or # Check the middle from top down
    (board[9] == mark and board[6] == mark and board[3] == mark) or # Check the right from top down
    (board[1] == mark and board[5] == mark and board[9] == mark) or # Check the diagonal from bottom left to top right
    (board[7] == mark and board[5] == mark and board[3] == mark)) # Check the diagonal from top left to bottom right

#  Function that uses the random module to randomly decide which player goes first
import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1 will go first.'
    else:
        return 'Player 2 will go first.'

# Function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):

    return (board[position] == ' ')

# Function that checks if the board is full and returns a boolean value (True or False)
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#  Function asks for a player's next position (as a number 1-9) and then uses the space_check function to see if it's a free position. If free, then returns the position for later use.
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):
        position = int(input('Please enter the position of your next marker: '))
    return position

#  Function asks player if they want to play again and returns a boolean True if they do.
def replay():
    return input('Do you wish to play again: Yes or NO? ').lower().startswith('y')

# ***************************************
# Primary script for the Tic Tac Toe Game
# ***************************************

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the Board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False

   # while game_on:
    while game_on:

        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
