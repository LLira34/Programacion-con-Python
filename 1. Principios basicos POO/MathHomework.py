# MathHomework.py - The while statement
print("MathHomework.py")

# Ask the user to enter a math problem.
problem = input("Enter a math problem, or 'q' to quit: ")

# Keep going until the user enters 'q' to quit
while(problem != 'q'):
    # Using eval()
    print("The answer to ", problem, "is: ", eval(problem))
    problem = input("Enter another math problem, or 'q' to quit: ")
