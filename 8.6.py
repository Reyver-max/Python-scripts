
""""
COMPCS100. Programming 1. 8.6 Numbering files lines
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""""

def main():
    filename = input("Enter the name of the file: ")

    try:

        file = open(filename, mode="r")

    except OSError:
        print(f"There was an error in reading the file.")
        return


    # If we want to process the file one line at the time,
    # for-loop is the easiest way to achieve it.
    # On every repetition of the loop the variable file_line
    # will automatically contain the next line from the file.
    # The loop will end when all the lines in the file
    # have been processed.
    counter = 0

    for idx, file_line in enumerate(file, start = 1):

        file_line = file_line.rstrip()

        counter += 1

        print(idx, file_line)

    # When the file has been processed, we should close it.
    file.close()


if __name__ == "__main__":
    main()
