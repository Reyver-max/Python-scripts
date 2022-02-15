"""
COMP.CS.100 Programming 1. 1.6.4.  Index raises to study benefits

Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""

def main():
    input_line = input("Enter the amount of the study benefits: ")
    Study_benefits = float(input_line)
    Index_raise = (Study_benefits * 1.17) / 100
    benefit_after_raise = Study_benefits + Index_raise
    print(
        "If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be",
        benefit_after_raise, "euros")
    #b)
    another_index_raise = (benefit_after_raise * 1.17) /100
    final = benefit_after_raise + another_index_raise
    print(
        "and if there was another index raise, the study \nbenefits would be as much as",
        final, "euros")



if __name__ == "__main__":
    main()