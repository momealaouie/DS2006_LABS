# Battle of Dices - Multiplayer Edition
# Now supports any number of players using nested lists!
# 
# The rules are:
# 
# Each player throws two dice of different sizes (D6 and D12).
# The player with the highest sum wins the round.  
# The first player to win 3 times is the winner.
#
# Players can now identify themselves with names/nicknames!

import random

def rollD6():
    """Roll a standard 6-sided dice."""
    return random.randint(1, 6)

def rollD12():
    """Roll a 12-sided dice."""
    return random.randint(1, 12)

print(" Welcome to Battle of Dices - Multiplayer Edition! ")

# Getting the number of players and their names
num_players = int(input("How many players will be playing? "))
player_names = []

for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ")
    player_names.append(name)

print(f"\nGreat! We have {num_players} players:")
for i, name in enumerate(player_names):
    print(f"Player {i + 1}: {name}")

# Initializing the List of Player Scores to have the value 0 in each position
player_scores = []
for i in range(num_players):
    player_scores.append(0)

# Initializing player rolls to have an empty list for each player
player_rolls = []
for i in range(num_players):
    player_rolls.append([])

rounds_played = 0
game_winner = None

while game_winner is None:
    input("\nPress ENTER to roll the dice...")
    
    # Store current round results
    current_round_totals = []
    
    print(f"\n--- Round {rounds_played + 1} ---")
    
    # Each player rolls their dice
    for i in range(num_players):
        dice1 = rollD6()
        dice2 = rollD12()
        total = dice1 + dice2
        
        # Store the rolls for this player
        player_rolls[i].append([dice1, dice2, total])
        current_round_totals.append(total)
        
        print(f"{player_names[i]} rolled:")
        print(f"  D6: {dice1}")
        print(f"  D12: {dice2}")
        print(f"  Total: {total}")
    
    # Find the highest score this round
    highest_score = max(current_round_totals)
    
    # Find all players with the highest score (for ties)
    round_winners = []
    for i in range(num_players):
        if current_round_totals[i] == highest_score:
            round_winners.append(i)
    
    # Update scores and display results
    if len(round_winners) == 1:
        winner_index = round_winners[0]
        player_scores[winner_index] += 1
        print(f"\n{player_names[winner_index]} wins this round!")
        print(f"Because {highest_score} was the highest score!")
    else:
        winner_names = [player_names[i] for i in round_winners]
        print(f"\nAmazing! This round has a tie between: {', '.join(winner_names)}")
        print(f"All tied players scored {highest_score}")
    
    rounds_played += 1
    
    # Display current scores
    print("\nCurrent scores:")
    for i in range(num_players):
        print(f"  {player_names[i]}: {player_scores[i]} wins")
    
    # Check whether or not there were winning player(s)
    for i in range(num_players):
        if player_scores[i] >= 3:
            game_winner = i
            break

# Announce the final winner
print(f"\n {player_names[game_winner]} destroys all opponents and is the newest Battle of Dices Champion!")
print(f"It took {rounds_played} rounds for {player_names[game_winner]} to win the game.")

# Save the results
print(f"\n--- Final Game Results ---")
print(f"Champion: {player_names[game_winner]}")
print(f"Total rounds played: {rounds_played}")
print("\nFinal scores:")
for i in range(num_players):
    print(f"  {player_names[i]}: {player_scores[i]} wins")

print("\nDetailed roll history:")
for i in range(num_players):
    print(f"\n{player_names[i]}'s rolls:")
    for round_num, roll_data in enumerate(player_rolls[i]):
        dice1, dice2, total = roll_data
        print(f"  Round {round_num + 1}: D6={dice1}, D12={dice2}, Total={total}")

print("\nThanks for playing Battle of Dices! ")