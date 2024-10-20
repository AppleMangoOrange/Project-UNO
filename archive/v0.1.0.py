'''
Project UNO v0.1.0
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
        self.value = value

    def __str__(self):
        #return f"{self.colour}, {self.value}"
        return "{colour}, {value}".format(colour = self.colour.name, value = self.value.name)


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
