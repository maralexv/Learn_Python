"""
Task: Create a Tic Tac Toe game.

Requirements:
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
Programme should be able to ask for an input of the player position, accept it
and then place a symbol on the board. Programme should be able to check if
someone has won, too, announce the winner and offer replay.

"""

import random

def display_board(board):
    """Displays the 'board' with marks ('X' and 'O'), assigned to positions"""
    #print('\n'*100)
    print(f"{board[0]} | {board[1]} | {board[2]}\n\
---------\n{board[3]} | {board[4]} | {board[5]}\n\
---------\n{board[6]} | {board[7]} | {board[8]}\n")


#test_board = ['X', 2, 'O', 4, 'X', 6, 7, 8, 9]
#display_board(test_board)


def space_check(board, position):
    """Checks if the position chosen is empty/free and tells to replay if it is not"""
    if board[position-1] in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        return True
    else:
        return False


#print(space_check(test_board, 2))


def player_input(board, playe_r):
    """Ask player for position (1 through 9), where he/she wants to play"""
    while True:
        position = int(input(f"{playe_r}, please tell me the position, where you would like to play: "))
        if position not in range(1, 10):
            print("Sorry, but you can choose only 1 through 9. Please try again")
        elif space_check(board, position):
            return position
        else:
            print("I am sorry, but this position is already occupied. Let's try again...")


#player_input(test_board)


def mark_position(board, mark, position):
    """Assign 'X' or 'O' (whichever the player plays to specified/chosen position"""
    board[position-1] = mark
    return board


#display_board(test_board)
#mark_position(test_board, "X", 9)
#display_board(test_board)


def check_hor(board):
    for i in range(0,7,3):
        if board[i] == board[i+1] and board[i] == board[i+2]:
            return True


def check_vert(board):
    for z in range(0, 3):
        if board[z] == board[z + 3] and board[z] == board[z + 6]:
            return True


def check_diag(board):
    if board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[2] == board[4] and board[2] == board[6]:
        return True


def win_ceck(board, player):
    """ Check if one of the players has won"""
    if check_hor(board) or check_vert(board) or check_diag(board):
        print(f"\n{player}, you have won!\n Game Over")
        return False
    else:
        return True


#test_board = ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'O']
#player = "Bob"
#display_board(test_board)
#win_ceck(test_board, player)


def replay():
    """Ask if the players want to play again, start a new game if yes, end if not"""
    que = input("Do you want to play one more time? ")
    if que in ("Yes", "yes", "Yeah", "yeah", "Yep", "yep", "Y", "y"):
        if assign_xo():
            setup = (player1, 'X', player2, 'O')
            print(
                f"\nThis round {setup[0]} shall play {setup[1]} and {setup[2]} shall play {setup[3]}.\n{setup[0]} starts.\n")
        else:
            setup = (player2, 'X', player1, 'O')
            print(
                f"\nThis round {setup[0]} shall play {setup[1]} and {setup[2]} shall play {setup[3]}.\n{setup[0]} starts.\n")

        a = input("Please press 'ENTER' key to continue.")
        the_game(setup)
    else:
        print("See you next time!")
        return None


def assign_xo():
    """Randomly assigns 'X' or 'O' to players"""
    if random.random() < .50000000001:
        return True

#print(assign_xo())


def the_game(gameset):
    """The actual game..."""
    theboard = [x for x in range(1, 10)]
    turn = 1
    player = gameset[0]
    display_board(theboard)

    while win_ceck(theboard, player):
        if turn == 10:
            break
        else:
            if turn % 2 == 0:
                marker = gameset[3]
                player = gameset[2]
            else:
                marker = gameset[1]
                player = gameset[0]

            position = player_input(theboard, player)
            mark_position(theboard, marker, position)
            display_board(theboard)
            if not win_ceck(theboard, player):
                break
            turn += 1


# Start the Game

print("\nWelcome to Tic Tak Toe!")

# Collect names of the players
player1 = input("\nPlayer 1, your name please: ")
player2 = input("\nPlayer 2, your name please: ")

# Players are randomly assigned what they will play with 'X' or 'O'
if assign_xo():
    setup = (player1, 'X', player2, 'O')
    print(f"\nThis round {setup[0]} shall play {setup[1]} and {setup[2]} shall play {setup[3]}.\n{setup[0]} starts.\n")
else:
    setup = (player2, 'X', player1, 'O')
    print(f"\nThis round {setup[0]} shall play {setup[1]} and {setup[2]} shall play {setup[3]}.\n{setup[0]} starts.\n")

a = input("Please press 'ENTER' key to continue.")

the_game(setup)
replay()
