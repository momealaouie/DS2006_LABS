# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws two dice of different sizes (D6 and D12).
# The player with the highest sum wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

def rollD6():
    """Roll a standard 6-sided dice."""
    return random.randint(1, 6)

def rollD12():
    """Roll a 12-sided dice."""
    return random.randint(1, 12)

print("🎲 Welcome to Battle of Dices - Two Dice Edition! 🎲")

player1_wins = 0
player2_wins = 0
rounds_played = 0

while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")
    
    player1_dice1 = rollD6()
    player1_dice2 = rollD12()
    player1_total = player1_dice1 + player1_dice2
    
    player2_dice1 = rollD6()
    player2_dice2 = rollD12()
    player2_total = player2_dice1 + player2_dice2
    
    rounds_played += 1
    
    print("Player 1 rolled:")
    print("  D6:", player1_dice1)
    print("  D12:", player1_dice2)
    print("  Total:", player1_total)
    
    print("Player 2 rolled:")
    print("  D6:", player2_dice1)
    print("  D12:", player2_dice2)
    print("  Total:", player2_total)
    
    current_round_winner = None
    
    if player1_total > player2_total:
        current_round_winner = "Player 1"
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because", player1_total, "is greater than", player2_total)
    elif player1_total == player2_total:
        current_round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
        print("Both players scored", player1_total)
    else:
        current_round_winner = "Player 2"
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because", player2_total, "is greater than", player1_total)
    
    print("Result of this round:", current_round_winner)
    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")

if player1_wins == 3:
    print("Player 1 destroys Player 2 and is the newest Battle of Dices Champion! ")
    print("It took", rounds_played, "rounds for Player 1 to win the game.")
elif player2_wins == 3:
    print("Player 2 destroys Player 1 and is the newest Battle of Dices Champion! ")
    print("It took", rounds_played, "rounds for Player 2 to win the game.")