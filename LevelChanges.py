""""
COMPCS100. Programming 1. 6.2 Level Changes in Seawater
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""
"""This is a program that calculates the statistical calculations
 of the level changes in the seawater"""

from math  import sqrt

def read_input():
    """ This function asks thh user to enter the sealevel measurements he wants
   to calculate the mean, variance and standard deviation.
    This numbers will be stored in an empty list in order to make the calculations.
    The program stops when the user enters an empty line

    There are not parameters set in this function"""

    numbers = []
    print(f"Enter seawater levels in centimeters one per line.\nEnd by entering an empty line.\n ")
    index = 0

    while True:
        n = input()
        index += 1

        if n == "":
            break
        else:
            f = float(n)
            numbers.append(f)
    if len(numbers) < 3:
        print("Error: At least two measurements must be entered!")
        return False

    # The minimum value entered in the list
    minimum =(f"{min(numbers):.2f}")
    print(f"Minimum:{minimum.rjust(9)} cm")
    
    # The maximun value entered in the list
    maximum =(f"{max(numbers):.2f}")
    print(f"Maximum: {maximum.rjust(10)} cm")

    # The median function defined below
    median =(f"{calculate_median(numbers):.2f}")
    print(f"Median: {median.rjust(10)} cm")

    # The mean function defined below
    m =(f"{mean(numbers):.2f}")
    print(f"Mean: {m.rjust(10)} cm")

    # The variance function, in order to get the variance of the mean to be able to calculate the Std. Dev.
    variance(numbers)

    # The Standard Deviation function
    sd =(f"{standard_deviation(numbers):.2f}")
    print(f"Deviation: {sd.rjust(10)} cm")



def mean(cal):
    """This function calculates the mean of the entered numbers.
    parameters: it takes the list we just created in the first function as a parameter

    This function will be called in the read_input function"""

    average = sum(cal) / len(cal)
    return average

def variance(numbers):
    """ This function calculates the variance of the list. The Variance calculates
    how the measurements are spread around the mean of the list

    Parameters: the elements in the list 'numbers' """
    n = len(numbers)
    avg = sum(numbers) / n
    var = sum((i-avg)**2 for i in numbers)/ n-0
    return var

def standard_deviation(numbers):
    """This is a fucntion that calculates the Standard deviation of the list.
    First we need to calculate the variance in order to obtain the standard deviation

    Parameters: the elements of the list "Numbers" """

    # In order to obtain the standard deviation, we need to calculate the
    # square root of the variance
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev

def calculate_median(numbers):
    """This is a function that calculates the median of the given list
    parameters: the list of numbers """
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        median = (sorted_numbers[length//2-1] + sorted_numbers[length//2])/2
    else:
        median = sorted_numbers[length//2]
    return median

def main():
    read_input()
    #A function that calculates the median
# A function that calculates the mean
#A function that calculates the variance
#A function that calculates th standard deviation






if __name__ == "__main__":
    main()