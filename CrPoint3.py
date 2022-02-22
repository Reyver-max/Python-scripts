"""""
COMP.CS.100. Programming 1. 3.3  Project 1: Credit Point Calculator
Reyver Serna: rs412764@tuni.filte
Student number: 412764
"""""

def main():
    pointsEnd = 0
    months=int(input("Enter the number of months: "))
    total=0

    for i in range(months):
        points=float(input("Enter the number of credits in month {}: ".format(i+1)))
        if points == 0: #here is the new code
            pointsEnd += 1
            if pointsEnd == 2:
                end = print('You did have too many study breaks!')
                return end
                ()
        total += points

    average=total/months
    if average >= 5:
        print(f"You are a full time student and your monthly credit point average is {average:.1f}")
    elif average < 5:
        print(f"Your monthly credit point average {average:.1f} does not classify you as a full time student.")



if __name__ == "__main__":
    main()