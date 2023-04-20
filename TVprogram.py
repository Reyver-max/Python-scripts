"""
COMP.CS.100 Programming 1
9.5 Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.

Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    Parameters: the data stored in rows of the file.
    """

    movie_library = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            # TODO add the name and genres data to the data structure
            for genre in genres:
                if genre not in movie_library:
                    movie_library[genre] = []
                movie_library[genre].append(name)
        file.close()
        return movie_library


    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    
    filename = input("Enter the name of the file: ")
    read_file(filename)

    genre_data = read_file(filename)

    # TODO print the genres
    print(f'Available genres are: {", ".join([ genre for genre in sorted(genre_data.keys()) ]) }')

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        elif genre not in genre_data:
            continue

        # TODO print the series belonging to a genre.
        for movie in sorted(genre_data[genre]):
            print(movie)



if __name__ == "__main__":
    main()
