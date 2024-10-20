'''
This module accepts 
- a deck of cards (as a list), 
- the number of players
and returns 
- a dictionary where each player's hand is a list
'''


# Ask for the number of player playing
num_players = int(input("Enter the number of players (2-15): "))
# Check if the number of players is (2-15)
while not (num_players in range(2, 15+1)):
    # print("num_players: ", num_players)
    # print(num_players in range(2, 15+1))
    print("Please try again.")
    num_players = int(input("Enter the number of players (2-15): "))


# Distribute cards to players and store hands in dict. player_hands
player_hands = {}
for player in range(1, num_players+1):
    hand = []
    for i in range(7):
        hand.append(playing_deck.pop(-1))
    player_hands[player] = sorted(hand, 
        key=lambda card: (100*card.colour.value - card.num.value))

for i in player_hands:
    print(i, ": ", [str(item) for item in player_hands[i]])
# print("Deck: ", [str(item) for item in playing_deck])
# Example to print 1st player's 4th card
# print(player_hands[1][3].colour, player_hands[1][3].num)