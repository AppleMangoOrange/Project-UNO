'''
This module defines an 'Original Deck' which contains all UNO cards
in order
'''


from enum import Enum, auto


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
    def __init__(self, colour, number):
        self.colour = colour
        self.number = number

    def __str__(self):
        # Both forms are correct: 
        return f"{self.colour.name}, {self.number.name}"
        # return "{colour}, {num}".format(
        #     colour = self.colour.name,
        #     num = self.number.name,
        # )

def print_cards(stack: list):
    return [str(card) for card in stack]

def sort_cards(stack: list):
    stack.sort(key=lambda card: (card.colour.value, -card.number.value))

'''
Returns the sorted original deck of UNO cards in a list as
Card objects
If printing = True, returns a list of strings of the 
corresponding UNO cards
'''
def create_deck(printing: bool=False):
    original_deck = []

    for colour in list(Colours)[1:]:
        for number in Numbers:
            card = Card(colour, number)
            original_deck.append(card)
            if number != Numbers.ZERO:
                original_deck.append(card)
            #     print("Just appended: ", original_deck[-1], "*2")
            # else:
            #     print("Just appended: ", original_deck[-1])

    for wild_card in Wild:
        for i in range(4):
            original_deck.append(Card(Colours.BLACK, wild_card))
            # print("Just appended: ", original_deck[-1])

    # original_deck.sort(key=lambda card: (card.colour.value, -card.number.value))
    sort_cards(original_deck)
    if printing == False:
        return original_deck
    else:
        return [str(item) for item in original_deck]


if __name__ == '__main__':
    # Example card:
    c = Card(Colours.BLUE, Numbers.FOUR)
    print(c.colour, c.number)

    # Example deck:
    original_deck = create_deck()
    print("Playing Deck: ", print_cards(original_deck))
    print("Number of UNO cards:", len(original_deck))
