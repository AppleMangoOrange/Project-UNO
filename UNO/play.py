'''
This module defines functions for players' turns, effect of cards, and viable cards to play
'''


import deck


# def play_card_from_hand(last_played_card: deck.Card, player_hand: list) -> deck:

def draw_cards(deck: list, player_hand: list, number_of_cards: int):
    pass

# Returns the card to be added to the discard pile after the turn ends
# Returns None if no card is to be added
def turn(deck: list, last_played_card: deck.Card, turns_since_last_played: int, player_hand: list):
    # Drawing cards:
    if (turns_since_last_played == 0):
        # Wild Draw 4
        if (last_played_card.number == deck.Wild.WILD_DRAW_FOUR):
            draw_cards(deck, player_hand, 4)
            return None
        # Draw 2
        if (last_played_card.number == deck.Numbers.DRAW_TWO):
            draw_cards(deck, player_hand, 2)
            return None
    # Skipping turn:
        if(last_played_card.number == Numbers.SKIP):
            return None
