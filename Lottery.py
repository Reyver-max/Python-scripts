"""""
COMP.CS.100. Programming 1. 4.7 Lottery Probabilities"
Reyver Serna: rs412764@tuni.fi
Student number: 412764
"""""
def factorial(n):
    """
    Calculate the factorial of a positive integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def probability(total_balls, drawn_balls):
    """
    Calculate the probability of winning the jackpot in a lottery game.
    """
    if drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")
        return
    else:
        num_lines = factorial(total_balls) / (factorial(drawn_balls) * factorial(total_balls-drawn_balls))
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{int(num_lines)}")





def main():
    # Ask the user for the number of balls and drawn balls
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    if total_balls <= 0:
        print("The number of balls must be a positive number.")
    else:
        #drawn_balls = int(input("Enter the number of the drawn balls: "))
        if drawn_balls <= 0:
            print("The number of balls must be a positive number.")
        else:
            probability(total_balls, drawn_balls)




if __name__ == "__main__":
    main()