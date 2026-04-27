import random

def play_game():
    choices = ["stone", "paper", "scissors"]

    user = input("Enter stone / paper / scissors: ").lower()
    comp = random.choice(choices)

    print("Computer chose:", comp)

    if user == comp:
        print("Result: Draw 🤝")

    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("Result: You Win 🎉")

    else:
        print("Result: Computer Wins 💻")