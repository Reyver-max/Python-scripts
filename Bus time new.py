""""
COMPCS100. Programming 1. 5.7 bus time Table
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""

"""This is a program that gives the best bus time table"""


def main():
    """First we create a bus time table in a variable containing a list"""
    time_table = [630, 1015, 1415, 1620, 1720, 2000]



    """We  create a variable that asks for the user's inout"""
    time = int(input(f"Enter the time (as an integer): "))

    for i in range(len(time_table)):
        if time <= time_table[0] or time >= time_table[-1]:
            print('The next buses leave:', *time_table[:3], sep = "\n")
            break
        elif time <= time_table[1] and time >= time_table[0]:
            print('The next buses leave:', *time_table[1:4], sep="\n")
            break
        elif time <= time_table[2] and time >= time_table[1]:
            print('The next buses leave:', *time_table[2:5], sep="\n")
            break
        elif time <= time_table[3] and time >= time_table[2]:
            print('The next buses leave:', *time_table[3:6], sep="\n")
            break
        elif time <= time_table[4] and time <= time_table[3]:
            print('The next buses leave:', *time_table[4:6], sep="\n")
            break
        elif time <= time_table[-2] and time >= time_table[-3]:
            print('The next buses leave:', *time_table[-2:],sep ="\n")
            print(*time_table[0:1], sep ="\n")
            break
        elif time <= time_table[-1] and time >= time_table[-2]:
            print('The next buses leave:', *time_table[-1:],sep ="\n")
            print(*time_table[0:2], sep ="\n")
            break


if __name__ == "__main__":
    main()
