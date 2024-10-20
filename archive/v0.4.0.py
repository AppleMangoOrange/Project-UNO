'''
Project UNO v0.4.0
The UNO! card game deck has 108 cards:
    Four 0s in all four colours [ZERO*4] (4)
    Two of numbers 1-9 each in all four colours [ONE-NINE*8] (72)
    Two of Skip, Draw Two and Reverse in all four colours (24)
    Four Wild cards (4)
    Four Wild Draw Four cards (4)

At the start 7 cards are dealt to each player, and the player
to the left of the dealer plays first (unless action/wild card)

Player with 1 card remaining must call UNO!. If not caught or says UNO
before getting caught, no penalties apply. Can only be caught before
the next subsequent player plays their turn.

Wild Draw 4 can only be played if the player has no other cards of that
colour. If done anyway, only the next subsequent player can challenge.
If caught, penalty applies. If not caught, no penalty.

'''


from enum import Enum, auto
import random


# Defining of the original deck of UNO:
# Enum of suits in the deck + BLACK (for wild cards)
class Colours(Enum):
    BLACK = 0
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4

# Enum of all cards which can have colour
class Numbers(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    REVERSE = 10
    SKIP = 11
    DRAW_TWO = 12

# Enum of Wild cards
class Wild(Enum):
    WILD_CARD = auto()
    WILD_DRAW_FOUR = auto()

# Struct of cards holding the card colour and value
class Card:
    def __init__(self, colour, value):
        self.colour = colour
        self.num = num

    def __str__(self):
        # Both forms are correct: 
        #return f"{self.colour}, {self.value}"
        return "{colour}, {value}".format(colour = self.colour.name, value = self.num.name)

# Now we define the original deck of UNO cards
original_deck = []

for col in list(Colours)[1:]:
    for num in Numbers:
        card = Card(col, num)
        original_deck.append(card)
        if num != Numbers.ZERO:
            original_deck.append(card)
            #print("Just appended: ", original_deck[-1], "*2")
        #else:
            #print("Just appended: ", original_deck[-1])

for wild_card in Wild:
    card = Card(Colours.BLACK, wild_card)
    for i in range(4):
        original_deck.append(card)
        #print("Just appended: ", original_deck[-1], "*4")

#for card in original_deck:
#    print(card)


# Copy the original deck and shuffle the copy
playing_deck = original_deck.copy()
random.shuffle(playing_deck)

# for card in playing_deck:
#    print(card)
# print(len(original_deck) == len(playing_deck))


# Ask for the number of player playing
num_players = int(input("Enter the number of players (2-15): "))
# Check if the number of players is (1-15)
while not (num_players in range(2, 15+1)):
    # print("num_players: ", num_players)
    # print(num_players in range(2, 15+1))
    print("Please try again.")
    num_players = int(input("Enter the number of players (1-15): "))


# Distribute cards to players and store hands in dict. player_hands
player_hands = {}
for player in range(1, num_players+1):
    hand = []
    for i in range(7):
        hand.append(playing_deck.pop(0))
    player_hands[player] = sorted(hand, key=lambda card: (100*card.colour.value + (100-card.num.value)))

# for i in player_hands:
#     print(i, ": ", [str(item) for item in player_hands[i]])
# # print("Deck: ", [str(item) for item in playing_deck])
# # Example to print 1st player's 4th card
# print(player_hands[1][3].colour, player_hands[1][3].num)
