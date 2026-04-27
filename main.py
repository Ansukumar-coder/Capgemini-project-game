from game import play_game

def menu():
    while True:
        print("1. Play Game")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()