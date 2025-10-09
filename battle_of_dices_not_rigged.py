# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

from lab_battle_of_dices import rollD6

print("🎲 Welcome to Battle of Dices! 🎲")

player1_wins = 0
player2_wins = 0
rounds_played = 0  # Track the number of rounds

# Lists to store all rolls for each player
player1_rolls = []
player2_rolls = []

# Use a while loop to play rounds until someone wins 3 times
while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")
    player1_roll = rollD6()  # Using the rollD6() function from lab-battle-of-dices
    player2_roll = rollD6()  # Using the rollD6() function from lab-battle-of-dices
    
    # Store the rolls in their respective lists
    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)
    
    rounds_played += 1  # Increment round counter
    
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)
    
    current_round_winner = None
    
    if player1_roll > player2_roll:
        current_round_winner = "Player 1"
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player1_roll == player2_roll:
        current_round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
    else:
        current_round_winner = "Player 2"
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
    
    print("Result of this round:", current_round_winner)
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Determine and announce the winner
if player1_wins == 3:
    print("Player 1 destroys Player 2 and is the newest Battle of Dices Champion! ")
    print("It took", rounds_played, "rounds for Player 1 to win the game.")
elif player2_wins == 3:
    print("Player 2 destroys Player 1 and is the newest Battle of Dices Champion! ")
    print("It took", rounds_played, "rounds for Player 2 to win the game.")

# Display detailed game summary table

print("GAME SUMMARY TABLE")
print(f"{'Round':<8} {'Player 1':<10} {'Player 2':<10} {'Winner':<12} {'Status'}")

# Create summary using the stored lists
for round_num in range(rounds_played):
    p1_roll = player1_rolls[round_num]
    p2_roll = player2_rolls[round_num]
    
    # Determine round winner and status
    if p1_roll > p2_roll:
        winner = "Player 1"
        status = f"{p1_roll} > {p2_roll}"
    elif p1_roll == p2_roll:
        winner = "Tie"
        status = f"{p1_roll} = {p2_roll}"
    else:
        winner = "Player 2"
        status = f"{p2_roll} > {p1_roll}"
    
    print(f"{round_num + 1:<8} {p1_roll:<10} {p2_roll:<10} {winner:<12} {status}")



# Additional statistics using the lists
print(f" ADDITIONAL STATISTICS:")
print(f"Total rounds played: {len(player1_rolls)}")
print(f"Player 1 - Highest roll: {max(player1_rolls)}, Lowest roll: {min(player1_rolls)}")
print(f"Player 2 - Highest roll: {max(player2_rolls)}, Lowest roll: {min(player2_rolls)}")

# Calculate and display average rolls (NEW MATHEMATICAL OPERATION)
player1_average = sum(player1_rolls) / len(player1_rolls)
player2_average = sum(player2_rolls) / len(player2_rolls)
print(f"Player 1 - Average roll: {player1_average:.2f}")
print(f"Player 2 - Average roll: {player2_average:.2f}")

# Determine who had better luck on average
if player1_average > player2_average:
    print(f"Player 1 had better luck on average! ({player1_average:.2f} vs {player2_average:.2f})")
elif player2_average > player1_average:
    print(f"Player 2 had better luck on average! ({player2_average:.2f} vs {player1_average:.2f})")
else:
    print(f"Both players had exactly the same average luck! ({player1_average:.2f})")

print("Thanks for playing Battle of Dices! 🎲")

filename = input("Enter the filename to save the results: ")

with open(filename, 'w') as file: # "w" = write mode
    for i in range(len(player1_rolls)):
        file.write(f"Round {i+1}: Player 1 rolled {player1_rolls[i]}, Player 2 rolled {player2_rolls[i]}\n")