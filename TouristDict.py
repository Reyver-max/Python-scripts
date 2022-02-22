""""
COMPCS100. Programming 1. 7.5 A Tourist Dictionary
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}
    cont = ", ".join(sorted(english_spanish))
    print(f"Dictionary contents:\n{cont}")

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish.get(word)}")
            if word not in english_spanish:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            k = input("Give the word to be added in English: ")
            p = input("Give the word to be added in Spanish: ")
            new = {k:p}
            english_spanish.update(new)
            inv_map = {v: k for k, v in english_spanish.items()}
            spanish_english.update(inv_map)
            cont = ", ".join(sorted(english_spanish))
            print(f"Dictionary contents:\n{cont}")



        elif command == "R":
            word = input("Give the word to be removed: ")
            del english_spanish[word]
            continue


        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            print()
            print("English-Spanish")
            for k, v in sorted(english_spanish.items()):
                print(k,v)
            print()
            print("Spanish-English")
            for k, v in sorted(spanish_english.items()):
                print(k,v)
            print()



        elif command == "T":
            translate = input(f"Enter the text to be translated into Spanish: ")
            lst = translate.split()
            for i in lst:
                t = english_spanish.get(i)
                if t in english_spanish:
                    print(f"The text, translated by the dictionary: \n{t}")



        else:
            print("Unknown command, enter W, A, R, P, T or Q!")
if __name__ == '__main__':
    main()