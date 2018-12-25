# SayMyName.py

# Ask the user for their name
name = input("What is your name? ")

# Print their name 100 times
for x in range(1, 101, 5):
    # Print their name followed by space, no a new line.
    print(x, name, end=" ")
