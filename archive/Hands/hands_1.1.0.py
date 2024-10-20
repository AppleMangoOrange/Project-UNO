'''
This module accepts 
- a deck of cards (as a list), 
- the number of players
and returns 
- a dictionary where each player's hand is a list
'''

num_players = -1
'''
Returns the number of players playing, asking for input 
when the current value is < 0, retrying if  outside the 
given range
'''
def NumberPlayers(
    minimum: int = 2, 
    maximum: int = 15, 
    new_value: bool = False, 
    ):
    global num_players
    if (new_value == True) or (num_players < 0):
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




# Distribute cards to players and store hands in dict. player_hands
for i in player_hands:
    print(i, ": ", [str(item) for item in player_hands[i]])
# print("Deck: ", [str(item) for item in playing_deck])
# Example to print 1st player's 4th card
# print(player_hands[1][3].colour, player_hands[1][3].num)

def PlayerHands(num_players: int = NumberPlayers(2, 15, True)):
    player_hands = {}
    for player in range(1, num_players+1):
        hand = []
        for i in range(7):
            hand.append(playing_deck.pop(-1))
        player_hands[player] = sorted(hand, 
            key=lambda card: (100*card.colour.value - card.num.value))

