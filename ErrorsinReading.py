""""
COMPCS100. Programming 1. 8.4 Errors in reading inputs
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""""
def print_box(width, height, mark):
    """Define a function with the parameters for width,
    height and mark
    """

    box = ""

    for row in range(height):
        box += width * mark
        if row != height - 1:
            box += "\n"
        else:
            continue

    print(box)

def read_input():
    """This function read the user inputs"""

    start_loop = True



    while start_loop:
        width = input("Enter the width of a frame: ")
        try:
            width = int(width)
            if width < 0:
                break
        except ValueError:
            continue
        while start_loop:
            height = input("Enter the height of a frame: ")
            try :
                height = int(height)
                if height < 0:
                    break
            except ValueError:
                    continue

            mark = input("Enter a print mark: ")
            print()
            print_box(width, height, mark)
            start_loop = False



def main():
    read_input()


if __name__ == "__main__":
    main()