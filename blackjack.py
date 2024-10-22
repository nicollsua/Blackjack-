# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *



# multiplayer set up
print("Welcome to Blackjack!")
num_players = int(input("How many players? "))

# create list to input a dictionary for each player that contains names
# and hand values. followed by a for loop that iterates in the range of num_players
players = []
for i in range(num_players):
    player_name = input(f"What is player {i+1}'s name? ")
    players.append({'name': player_name, 'hand': 0, 'score': 3})



user_answer = ''
while user_answer != 'n':
    # players' turn: for loop that allows each player in players to take their TURN
    # making sure to update the 'hand' for each player in their dictionary
    for player in players:
        player['hand'] = draw_starting_hand(player['name'].upper())
        should_hit = 'y'
        while player['hand'] < 21:
            should_hit = input(f"You have {player['hand']}. Hit (y/n)? ")
            if should_hit == 'n':
                break
            elif should_hit != 'y':
                print("Sorry, I didn't get that.")
            else:
                player['hand'] += draw_card()
        print_end_turn_status(player['hand'])




    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
        print(f"Dealer has {dealer_hand}.")
        dealer_hand += draw_card()
    print_end_turn_status(dealer_hand)


    # GAME RESULT
    print_header('GAME RESULT')
    for player in players:
        print_end_game_status(player, dealer_hand)


    for i in range(len(players)):
      if players[i]['score'] == 0:
        players.pop(i)
    if len(players) == 0:
      print('All players eliminated!')
      user_answer = 'n'
    else:    # ask users if they want to play another round
      user_answer = input("Do you want to play another hand (y/n)? ")
