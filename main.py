# This is a rock-paper-scissors  game
# The aim is to create more complicated if structures

def main():
    # Define the players' inputs
    Player_1 = input("Player 1, enter your choice (R/P/S): ")
    answer = str(Player_1)
    Player_2 = input("Player 2, enter your choice (R/P/S): ")
    answer = str(Player_2)

    if Player_1 == 'P' and Player_2 == 'S':
        print("Player 2 won!")
    elif Player_1 == 'P' and Player_2 == 'R':
        print("Player 1 won!")
    if Player_1 == 'R' and Player_2 == 'P':
        print("Player 2 won!")
    elif Player_1 == 'R' and Player_2 == 'S':
        print("Player 1 won!")
    if Player_1 == 'S' and Player_2 == 'R':
        print("Player 2 won!")
    elif Player_1 == 'S' and Player_2 == 'P':
        print("Player 1 won!")
    else:
        if Player_1 == Player_2:
            print("It's a tie!")
if __name__ == "__main__":
    main()
