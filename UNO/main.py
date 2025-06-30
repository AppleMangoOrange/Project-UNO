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
from simple_term_menu import TerminalMenu

import deck, hands



# Returns the player number who has won, and 0 if no one has won
def win_condition():
    # TODO: build win condition
    pass


number_players = hands.get_number_players()

# Copy the original deck and shuffle the copy
playing_deck = deck.create_deck()
random.shuffle(playing_deck)

# Distribute cards to the players
player_hands = hands.distribute_player_hands(number_players, playing_deck)

# Define discard pile
discard_pile = []
# Add topmost card of playing deck to discard pile
while True:
    discard_pile.append(playing_deck.pop(-1))
    if not discard_pile[-1].is_special():
        break
print(f"Discard pile state: {discard_pile}")

def turn(current_player: int):
    global player_hands, discard_pile
    assert current_player < number_players

    hand = player_hands[current_player]
    current_card = discard_pile[-1]

    # current_card.functionality # TODO: Add card functionality

    print(f"\n\n === PLAYER {current_player + 1} === \n")
    print(f"Discard Pile: {current_card}")
    print(f"Your hand: {hand}")
    playable = hand.playable(current_card)
    prompt = TerminalMenu(
        [str(hand[i]) for i in playable] + ["Exit"], 
        title="Select a card to play:"
    ).show()
    if prompt == len(playable):
        exit(0)
    discard_pile.append(  hand.play(playable[prompt])  )

number_turns = 0
for i in range(5):
    turn(number_turns % number_players)
    number_turns += 1
