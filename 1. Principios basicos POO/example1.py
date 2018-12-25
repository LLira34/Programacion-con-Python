# example1.py
# --- task 1: define the event handle routines
def handle_A():
    print("Wrong! Try again!")

def handle_B():
    print("Absolutely right!")

def handle_C():
    print("Wrong! Try again!")

# --- task 2: define the appearance of the screen
print("\n"*100)
print("  VERY CHALLENGING GUESSING GAME")
print("="*50)
print("Press the letter of your answer, then the ENTER key.")
print("A. Animal")
print("B. Vegetal")
print("C. Mineral")
print()
print("X. Exit from this program.")
print("="*50)
print()
print("What type of thing is 'Carrot'")

# --- task 3: the event loop. We loop forever, observing events
while 1:
    answer = input().upper()
    if answer == "A": handle_A()
    if answer == "B": handle_B()
    if answer == "C": handle_C()
    if answer == "X":
        print("\n"*100)
        break;



