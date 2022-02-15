"COMPCS100. Programming 1. 4.11.1 Improved Box  a Box printing"
"Name: Reyver Serna"
"Email: rs412764@tuni.com"
"Student Number: 412764"


# TODO: the definition of print_box goes here unless it goes after main.
def print_box(width, height, border_mark="#", inner_mark=" " ):
    """[this is a fucntion that prints an improved box]
    the parameter are:
    height: integer
    width: integer
    inner_mark = str
    border_mark = str
    """
    box = ""

    width = int(width)
    height = int(height)
    for row in range(height):
        if row == 0 or row == height - 1:
            box += width * border_mark

            box += "\n"

        else:
            box += border_mark + (width - 2) * inner_mark + border_mark + "\n"

    print(box)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()