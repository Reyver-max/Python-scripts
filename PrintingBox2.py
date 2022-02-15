"COMPCS100. Programming 1. 3.8.2 Printing a Box and Checking inputs"
"Name: Reyver Serna"
"Email: rs412764@tuni.com"
"Student Number: 412764"

"""This is a programm for printing a box"""

def read_input(str):
    '''
    checking inputs and returning them
    :param str:
    :return:
    '''
    while True:
        width = int((input(str)))
        if int(width) > 0:
            return width
def read_input2(i=1):
    '''
    checking inputs and returning them
    :return:
    '''
    while True:
        width = (input("Enter the width of a frame: "))
        if int(width) > 0:
            break

    while True:
        height = (input("Enter the height of a frame: "))
        if int(height) > 0:
            break

    return width, height

def print_box(width, height, mark):
    '''
    :param wf:
    :param hf:
    :param pm:
    '''
    for i in range(int(height)):
        print(int(width) * mark)


def main():
    width, height = read_input2()
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()


