""""
COMPCS100. Programming 1. 8.9 Writing Numbered lines to a file
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""""

"""This is a programm  that reads an user message in the usual style, 
ending with an empty line, and then saves it to a file"""

def read_message(text_line):
    """The function reads the input entered by the user,
    saves the rows in a list, and returns the list. The entry of the input is
    terminated by entering an empty row. This empty row is not saved in list."""

    list = []
    index = 0

    while True:

        index += 1
        list.append(text_line)
        break


def main():
    filename = input("Enter the name of the file: ")

    try:
        # To be able to write into file the value of the
        # mode parameter for open must be "w" (write).
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    while True:
        text_line = input()
        read_message(text_line)
        if text_line == "":
            break

        # Everything which print would normally show on the screen
        # can be directed to a file by using the named parameter
        # file and passing a stream which was opened in "w" mode
        # as its value.
        counter = 0
        for idx, text_line in enumerate(save_file, start=1):
            text_line = text_line.rstrip()
            counter += 1
            print(counter,text_line, file=save_file)




    save_file.close()

    print(f"File {filename} has been written.")




if __name__ == "__main__":
    main()