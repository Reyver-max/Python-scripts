""""
COMPCS100. Programming 1. 6.4 Vowels and consonants
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""
def main():
    str=input("Enter a word: ")
    vowels=0
    consonants=0
    for i in str:
        if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u'or i == 'y'
        or i == 'E'or i == 'I'or i == 'O'or i == 'U'or i == 'Y'or i == 'A'):
            vowels = vowels+1 #vowel counter is incremented by 1
        else:
            consonants=consonants+1 #consonant counter is incremented by 1
    print(f"The word \"{str}\" contains {vowels} vowels and {consonants} consonants.")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
