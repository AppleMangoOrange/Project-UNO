'''
This module accepts 
- a deck of (shuffled) cards (as a list), 
- the number of players
and returns 
- a dictionary where each player's hand is a list
'''

import deck

num_players = -1
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
    if (new_value == True) or (num_players < 1):
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


def distribute_player_hands(number_players: int, playing_deck: list, number_cards: int = 7) -> list[list]:
    player_hands = []
    for player in range(1, number_players+1):
        hand = [] # Initial hand state
        for i in range(number_cards): # Default 7 cards per player
            # Take last card from playing deck to add to hand
            hand.append(playing_deck.pop(-1))
        deck.sort_cards(player_hands[player])
    return player_hands


if __name__ == '__main__':
    print(get_number_players())
    print(get_number_players()) # Test for new_value

