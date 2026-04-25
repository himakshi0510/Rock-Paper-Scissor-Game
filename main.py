from game_logic import game
while True:
    print("\n --options:--")
    print("1. Play Game 🐍")
    print("2. Exit Game 🔚")
    choice = int(input("Enter Your Choice: "))
    if choice==1:
        print("Starting the game...")
        game()
    elif choice == 2:1
        print("Exiting the game...")
        break
    else:
        print("Invalid Option...")
