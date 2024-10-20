'''
Project UNO v0.6.0
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


import random

import deck
import hands


# Returns the player number who has won, and 0 if no one has won
def win_condition():
    # TODO: build win condition
    return 0


number_of_players = hands.get_number_players()

# Copy the original deck and shuffle the copy
playing_deck = deck.create_deck()
random.shuffle(playing_deck)
# print("Playing Deck: ", [str(item) for item in playing_deck])

player_hands = hands.distribute_player_hands(number_of_players, playing_deck)

discard_pile = []
# Add topmost card of playing deck to discard pile
discard_pile.append(playing_deck.pop(-1))


