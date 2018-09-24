"""
Task: Create a Tic Tac Toe game.

Here are the requirements:
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
Programme should be able to accept input of the player position and then place a
symbol on the board.

"""

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
