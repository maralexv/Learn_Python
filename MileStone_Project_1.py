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
    print('\n'*100)
    print(f"{board[0]} | {board[1]} | {board[2]}\n\
---------\n{board[3]} | {board[4]} | {board[5]}\n\
---------\n{board[6]} | {board[7]} | {board[8]}\n")


#test_board = ['', 2, 3, 4, 5, 6, 7, 8, 9]
#display_board(test_board)


def space_check(board, position):
    """Checks if the position chosen is empty/free and tells to replay if it is not"""
    if not board[position-1]:
        return True
    else:
        return False


#print(space_check(test_board, 1))


def player_input(board):
    """Ask player for position (1 through 9), where he/she wants to play"""
    while True:
        position = int(input("Please tell me the position, where you would like to play: "))
        if position not in range(1, 10):
            print("Sorry, but you can choose only 1 through 9. Please try again")
        elif space_check(board, position):
            return position
        else:
            print("I am sorry, but this position is already occupied. Let's try again...")


#test_board = ['', 'X', '', '', 'O', 'X', '', '', 'O']
#player_input(test_board)


def mark_position(board, mark, position):
    """Assign 'X' or 'O' (whichever the player plays to specified/chosen position"""
    board[position-1] = mark


def win_ceck(board):
    """ Check if one of the players has won"""
    return True


def replay():
    """Ask if the players want to play again, start a new game if yes, end if not"""
    que = input("Do you want to play one more time? ")
    if que in ("Yes", "yes", "Yeah", "yeah", "Yep", "yep", "Y", "y"):
        the_game()
    else:
        print("See you next time!")
        return None


def the_game():
    """The actual game..."""
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    position = 1
    turn = 1
    display_board(board)

    while win_ceck(board):
        if turn % 2 == 0:
            marker = p2
        else:
            marker = p1

        player_input(board)
        mark_position(board, marker, position)
        display_board(board)

        turn += 1



# Start the Game
print("Welcome to Tic Tak Toe!")

# Collect names of the players
player1 = input("\nPlayer 1, your name please: ")
player2 = input("\nPlayer 2, your name please: ")

# Player 1 chooses whether he/she will play as 'X' or 'O'
while True:
    p1 = input(f"\n{player1}, will you play 'X' or 'O'? Please choose: ")
    if p1 not in ('X', 'x', 'O', 'o'):
        print("Sorry, wrong input. You should indicate 'X' or 'O' (letters). Please try again.")
    else:
        print("\nThanks")
        break

# The choice of Player 1 determines what Player 2 will play
if p1 == "X" or p1 == "x":
    p2 = "O"
else:
    p2 = "X"

print(f"Good. In this case, {player2}, you will be playing '{p2}'.\n")

the_game()
replay()



