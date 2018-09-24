"""
Task: Create a Tic Tac Toe game.

Requirements:
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
Programme should be able to ask for an input of the player position, accept it
and then place a symbol on the board. Programme should be able to check if
someone has won, too, announce the winner and offer replay.

"""


def display_board(board):
    """Displays the 'board' with marks ('X' and 'O'), assigned to positions"""
    pass


def space_check(board):
    """Checks if the position chosen is empty/free and tells to replay if it is not"""
    pass


def player_input():
    """Ask player for position (1 through 9), where he/she wants to play"""
    pass


def mark_position(board, mark, position):
    """Assign 'X' or 'O' (whichever the player plays to specified/chosen position"""
    pass


def win_ceck(board, mark):
    """ Check if one of the players has won"""
    pass


def replay():
    """Ask if the players want to play again, start a new game if yes, end if not"""
    pass


# Start the Game
print("Welcome to Tic Tak Toe!")

# Collect names of the players
player1 = input("\nPlayer 1, your name please: ")
player2 = input("\nPlayer 2, your name please: ")

# Player 1 chooses whether he/she will play as 'X' or 'O'
p1 = input(f"\n{player1}, will you play 'X' or 'O'? Please choose: ")

# The choice of Player 1 determines what Player 2 will play
if p1 == "X" or p1 == "x":
    p2 = "O"
else:
    p2 = "X"

print(f"\nIn this case, {player2}, you will be playing '{p2}'.")
