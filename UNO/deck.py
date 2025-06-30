'''
This module defines an 'Original Deck' which contains all UNO cards
in order
'''


from enum import Enum, auto
import functools


# Defining of the original deck of UNO:
# Enum of suits in the deck + BLACK (for wild cards)
class _Colours(Enum):
    BLACK = 0
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4

# Enum of all cards which can have colour
class _Numbers(Enum):
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
class _Wild(Enum):
    WILD_CARD = auto()
    WILD_DRAW_FOUR = auto()

# Struct of cards holding the card colour and value
@functools.total_ordering
class Card:
    
    key = lambda card: (card.colour.value, -card.number.value)
    special = {
        _Colours: [_Colours.BLACK],
        _Numbers: [_Numbers.REVERSE, _Numbers.SKIP, _Numbers.DRAW_TWO]
    }

    def __init__(self, colour: _Colours, number: _Numbers):
        self.colour = colour
        self.number = number

    def __str__(self):
        return f"Card({self.colour.name}, {self.number.name})"
    
    __repr__ = __str__
    
    def __eq__(self, other):
        return (self.colour == other.colour) and (self.number == other.number)
    
    def __lt__(self, other):
        if self.colour.value < other.colour.value: return True
        elif self.colour.value == other.colour.value:
            if self.number.value > other.number.value: return True
        return False

    def __matmul__(self, other):
        '''
        Returns True if self can be played over other
        '''
        if self.colour == _Colours.BLACK:
            return True
        elif self.colour == other.colour:
            return True
        elif self.number == other.number:
            return True
        else:
            return False

    def is_special(self):
        return self.colour in Card.special[_Colours] or \
            self.number in Card.special[_Numbers]


def print_cards(stack: list):
    return [str(card) for card in stack]

def create_deck(printing: bool=False):
    '''
    Returns the sorted original deck of UNO cards in a list as
    Card objects
    If printing = True, returns a list of strings of the 
    corresponding UNO cards
    '''
    original_deck = []

    for colour in list(_Colours)[1:]:
        for number in _Numbers:
            card = Card(colour, number)
            original_deck.append(card)
            if number != _Numbers.ZERO:
                original_deck.append(card)
            #     print("Just appended: ", original_deck[-1], "*2")
            # else:
            #     print("Just appended: ", original_deck[-1])

    for wild_card in _Wild:
        for i in range(4):
            original_deck.append(Card(_Colours.BLACK, wild_card))
            # print("Just appended: ", original_deck[-1])

    # original_deck.sort(key=lambda card: (card.colour.value, -card.number.value))
    original_deck = sorted(original_deck)
    if printing == False:
        return original_deck
    else:
        return print_cards(original_deck)

if __name__ == '__main__':
    # Example card:
    c1 = Card(_Colours.BLUE, _Numbers.FOUR)
    print(c1.colour, c1.number)
    print("Special:", Card(_Colours.BLUE, _Numbers.REVERSE).is_special())

    # Example deck:
    original_deck = create_deck()
    # print(original_deck)

    # Card Sorting
    import random
    bunch = random.sample(original_deck, 10)
    print(f"Random bunch: {bunch}")
    bunch.sort()
    print(f"Sorted: {bunch}")
