# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D20.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

player1_wins = 0
player2_wins = 0

# Lists to store all rolls for the summary table
player1_rolls = []
player2_rolls = []
round_winners = []

round_num = 1

# Main game loop - continues until someone wins 3 rounds
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_num} ---")
    input("Press ENTER to roll the dice...")
    
    # Roll the dice for both players
    player1_roll = random.randint(1, 20)
    player2_roll = random.randint(1, 20)
    
    # Store the rolls
    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)
    
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)
    
    # Determine round winner
    if player1_roll > player2_roll:
        current_round_winner = "Player 1"
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because", player1_roll, "is greater than", player2_roll)
    elif player1_roll == player2_roll:
        current_round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
    else:
        current_round_winner = "Player 2"
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because", player2_roll, "is greater than", player1_roll)
    
    # Store the round winner
    round_winners.append(current_round_winner)
    
    print("Result of this round:", current_round_winner)
    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    
    round_num += 1

# Announce the final winner
print("\n" + "="*50)
if player1_wins == 3:
    print("Player 1 destroys Player 2 and is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 destroys Player 1 and is the newest Battle of Dices Champion! ")

# Display the round-by-round summary table
print("\n" + "="*50)
print("GAME SUMMARY - ROUND BY ROUND")
print("="*50)

# Create the table header
total_rounds = len(player1_rolls)
header = "| Round    |"
for i in range(1, total_rounds + 1):
    header += f" {i:2d} |"

# Create separator line
separator = "-" * len(header)

print(separator)
print(header)
print(separator)

# Player 1 row
player1_row = "| Player 1 |"
for roll in player1_rolls:
    player1_row += f" {roll:2d} |"
print(player1_row)

print(separator)

# Player 2 row
player2_row = "| Player 2 |"
for roll in player2_rolls:
    player2_row += f" {roll:2d} |"
print(player2_row)

print(separator)

# Winners row (optional - shows who won each round)
winners_row = "| Winner   |"
for winner in round_winners:
    if winner == "Player 1":
        winners_row += " P1 |"
    elif winner == "Player 2":
        winners_row += " P2 |"
    else:  # Tie
        winners_row += " -- |"
print(winners_row)

print(separator)

print(f"\nFinal Score: Player 1: {player1_wins} wins, Player 2: {player2_wins} wins")
print("Thanks for playing Battle of Dices! 🎲")