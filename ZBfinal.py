"""""
COMP.CS.100. Programming 1. 2.4.1 Number series game Zip Boing using for loop
Reyver Serna: rs412764@tuni.filte
Student number: 412764
"""""

def main():
    number =int(input("How many numbers would you like to have? "))

    for i in range(1, number+1):

        if i%3 == 0  and i%7 ==0:
            print("zip boing")

        elif i%3==0:
            print("zip")

        elif i%7==0:
            print("boing")
        else:
            print(i)

if __name__ == "__main__":
    main()
