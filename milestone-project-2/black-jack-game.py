"""
In this milestone project you will be creating a Complete BlackJack Card Game in Python.
Here are the requirements:
    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    T he player can 'stand' or 'hit'.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

You must use OOP and classes in some portion of your game. You can not just use functions
in your game. Use classes to help you define the Deck and the Player's hand. There are
many right ways to do this, so explore it well!

"""

# DEFINE THE GAME:
"""
Game Play
To play a hand of Blackjack the following steps must be followed:
    1. Create a deck of 52 cards
    2. Shuffle the deck
    3. Ask the Player for their bet
    4. Make sure that the Player's bet does not exceed their available chips
    5. Deal two cards to the Dealer and two cards to the Player
    6. Show only one of the Dealer's cards, the other remains hidden
    7. Show both of the Player's cards
    8. Ask the Player if they wish to Hit, and take another card
    9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the 
        Dealer's value meets or exceeds 17
    11. Determine the winner and adjust the Player's chips accordingly
    12. Ask the Player if they'd like to play again
    
Playing Cards
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) 
and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a 
total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a
rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in 
your program, you may want to assign variables to store a list of suits, ranks, and then
use a dictionary to map ranks to values.
"""

import random

# SET UP GLOBAL VARIABLES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


# DEFINE CARD
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


# DEFINE DECK
class Deck():

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                pass

    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        pass