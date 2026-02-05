# Import the random module for generating random numbers
import random

# Roll two dice and calculate initial total
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

# Loop until snake eyes (total = 2)
while total != 2:
    print("Nope")  # Print message as required
    # Reroll the dice and recalculate total
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

# Print success message after getting snake eyes
print("Snake eyes!")