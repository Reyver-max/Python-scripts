"COMPCS100. Programming 1. 3.8.2 Printing a Box and Checking inputs"
"Name: Reyver Serna"
"Email: rs412764@tuni.com"
"Student Number: 412764"

"""This is a programm for printing a box"""


def print_box(width, height, mark):
    """Define a function with the parameters for width,
    height and mark
    """

    for i in range(0, width):
        for j in range(0, height):
            if (i == 0 or i == width - 1 or j == 0 or j == height - 1):
                print(mark, end='  ')
            else:
                print(mark, end='  ')
        print()


def read_input(user):
    """This function read the user inputs"""
    if width <= 0 and height <= 0:
        return print_box(width, height, mark)


def main():
    # input is your friend here
    width = int(input("Please enter the width of the box: "))

    # width = print(int("Please enter the width of the box: "))
    # input etc..

    height = int(input("Please enter the height of the box: "))

    mark = input("Enter a print mark: ")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()