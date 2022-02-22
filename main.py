"""""
COMP.CS.100. Programming 1. 3.3  Project 1: Credit Point Calculator
Reyver Serna: rs412764@tuni.filte
Student number: 412764
"""""
import sys
def main():

    months = int(input("Enter the number of months: "))

    sum = 0
    counter = 1
    last_integer = None


    while counter <= months:
        credits_gained = int(input(f"Enter the number of credits in month{counter}: "))
        # if statement to validate that if the last_integer and credits
        # are equal and credits is zero then break the loop
        if credits_gained == last_integer and credits_gained == 0:
            break
            print()
            print("You did have too many study breaks!")

        else:
            sum += credits_gained
        counter +=1


    average = sum / months
    if average >=5:
        print()
        print(f'You are a full time student and your monthly credit point average is {average:.1f}.')
    if average <5:
        print()
        print(f"Your monthly credit point average {average:.1f} does not classify you as a full time student")


if __name__ == "__main__":
    main()
