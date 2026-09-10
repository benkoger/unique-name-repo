# This file simulates flipping a coin 100 times.
# Each heads result gives the user +1 dollar,
# and each tails result takes away 1 dollar.
# The script then reports the final balance and draws a plot
# showing how the balance changed over time.

# Import the random module so we can simulate coin flips.
import random

# Import matplotlib so we can make a line chart.
import matplotlib.pyplot as plt

# Start with a balance of 0 dollars.
balance = 0

# Create a list to store the balance after each flip.
# We will record the balance after every single toss.
balances = [0]

# Repeat the coin flip process 100 times.
for flip_number in range(1, 101):
    # Randomly choose either 0 or 1.
    # We treat 0 as tails and 1 as heads.
    result = random.randint(0, 1)

    # If the result is 1, the coin landed on heads.
    # Heads means the user gains 1 dollar.
    if result == 1:
        balance = balance + 1

    # Otherwise, the coin landed on tails.
    # Tails means the user loses 1 dollar.
    else:
        balance = balance - 1

    # Save the new balance after this flip.
    balances.append(balance)

# Print the final amount of money left.
print(f"After 100 coin flips, the user has ${balance}.")

# Create a list of flip numbers from 1 to 100.
flips = list(range(1, 101))

# Draw a line graph showing the balance over time.
plt.plot(flips, balances[1:])

# Add labels to explain the axes.
plt.xlabel("Flip number")
plt.ylabel("Money balance")
plt.title("Money Over 100 Coin Flips")

# Save the plot to a file so it is still created in headless environments.
plt.tight_layout()
plt.savefig("coin_flip_balance.png")

# Try to display the plot if a graphical environment is available.
try:
    plt.show()
except Exception:
    pass
