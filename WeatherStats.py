""""
COMPCS100. Programming 1.
Project 2: Weather Statistics
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""

"""This is a program that analyzes the temperatures measurements 
and figures out cold days and warm days and prints the results"""

"""Define the user_input function"""
def user_input(Temperatures):
    """This is a function that asks for user's input and stores it in a list.
     Parameters --> 'Temperatures':A variable that contains an empty list where the  inputs are stored"""

    # Set the variable with an empty list where the temperatures will be stored
    #Temperatures = []

    # Ask for the number of days from which we want the temperatures
    days=int(input("Enter amount of days: "))

    #For-loop to introduce the temperatures of each day
    for i in range(days):
        day_temp =float(input("Enter day {}. temperature in Celcius: ".format(i+1)))
        Temperatures.append(day_temp)
    print()


"""Define the function that calculates the mean and the median of input temperatures"""
def  mean_and_median(Temperatures):
    """This is a function that print the mean and the median of the input temperatures.
    Parameters ---> The list filled with the temp. inputs from the previous function"""

    #Calculate the mean of the list in a manual way and print it.
    mean = sum(Temperatures)/ len(Temperatures)
    print(f"Temperature mean: {mean:.1f}C")

    #calculate the median of the list in a manual way and print it.
    l=len(Temperatures)
    s = sorted(Temperatures)
    median = (s[l//2-1]/2.0+s[l//2]/2.0, s[l//2])[l % 2] if l else None
    print(f"Temperature median: {median:.1f}C")
    print()


"""Define the function the prints the days with temps over or equal to the median"""
def over_median(Temperatures):
    """This is a function that calculates and prints the days temps. over or equal
    to the median, as well as their difference to the mean
    Parameters: the elements of the list temperature"""

    #Calculate the mean of the list in a manual way.
    mean = sum(Temperatures)/ len(Temperatures)

    #calculate the median of the list in a manual way.
    l =len(Temperatures)
    s = sorted(Temperatures)
    median = (s[l//2-1]/2.0+s[l//2]/2.0, s[l//2])[l % 2] if l else None
    
    print(f"Over or at median were: ")
    
    for num, i in enumerate(Temperatures, start=1):

        if i >= median:
            difference_to_mean = (f"{i - mean:5.1f}C")
            i= (f"{i:5.1f}")
            num = (f"{num:2}")
            print("Day {}. {}C difference to mean:".format(num,i), difference_to_mean)
    print()
           

"""Define the function that prints the days with the temps under the median """
def under_median(Temperatures):
    """This is a function that calculates and prints the days temps. under
    the median, as well as their difference to the mean
    Parameters: the elements of the list temperature"""

    # Calculate the mean of the list in a manual way.
    mean = sum(Temperatures) / len(Temperatures)

    # calculate the median of the list in a manual way.
    l = len(Temperatures)
    s = sorted(Temperatures)
    median = (s[l // 2 - 1] / 2.0 + s[l // 2] / 2.0, s[l // 2])[
        l % 2] if l else None

    print(f"Under median were: ")

    for num, i in enumerate(Temperatures, start=1):
        if i < median:
            difference_to_mean = (f"{i - mean:5.1f}C")
            i= (f"{i:5.1f}")
            num = (f"{num:2}")
            print("Day {}. {}C difference to mean:".format(num, i),difference_to_mean)


def main():
    Temperatures = []
    user_input(Temperatures)
    mean_and_median(Temperatures)
    over_median(Temperatures)
    under_median(Temperatures)

if __name__ == "__main__":
    main()
