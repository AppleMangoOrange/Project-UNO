'''
This module accepts 
- a deck of (shuffled) cards (as a list), 
- the number of players
and returns 
- a dictionary where each player's hand is a list
'''


from collections.abc import Sequence

import deck
from deck import Card


num_players = None


class Hand(Sequence):
    def __init__(self, hand:list[Card]=[]):
        self.hand = sorted(hand)

    def __str__(self):
        return f"Hand(\n\t{'\n\t'.join(str(c) for c in self.hand)}\n)"

    __repr__ = __str__

    def __len__(self):
        return self.hand.__len__()

    def __getitem__(self, index: int):
        return self.hand[index]
    
    def append(self, card: Card) -> None:
        self.hand.append(card)
        self.hand.sort()
    
    def sort(self) -> None:
        self.hand.sort()

    def playable(self, card: Card) -> list[int]:
        '''
        Returns the indices of the playable Cards in hand against the given card
        '''
        return [i for i in range(len(self.hand)) if self.hand[i] @ card]

    def play(self, index: int) -> None:
        '''
        Removes and returns the card from hand at index
        '''
        return self.hand.pop(index)

'''
Returns the number of players playing, asking for input 
when the current value is < 1, retrying if  outside the 
given range
'''
def get_number_players(
    minimum: int = 2, 
    maximum: int = 15, 
    new_value: bool = False, 
    ):
    global num_players
    if (new_value) or (not num_players):
        num_players = int(input(
            f"Enter the number of players ({minimum}-{maximum}): "))
        # Check if the number of players is (minimum-maximum) (i.e. 2-15)
        while not (num_players in range(minimum, maximum+1)):
            # print("num_players: ", num_players)
            # print(num_players in range(minimum, maximum+1))
            print("Please try again.")
            num_players = int(input(
                f"Enter the number of players ({minimum}-{maximum}): "))
    return num_players


def distribute_player_hands(number_players: int, playing_deck: list, number_cards: int = 7) -> list[Hand]:
    player_hands = [None] * number_players
    for player in range(number_players):
        hand = Hand() # Initial hand state
        for i in range(number_cards): # Default 7 cards per player
            # Take last card from playing deck to add to hand
            hand.append(playing_deck.pop())
        hand.sort()
        player_hands[player] = hand
    return player_hands
  

if __name__ == '__main__':
    print(get_number_players())
    print(get_number_players()) # Test for new_value

