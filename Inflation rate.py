"""""
COMP.CS.100. Programming 1. 3.3  Project 1: Inflation Calculator
Reyver Serna: rs412764@tuni.filte
Student number: 412764
"""""
# You will implement a program which can be used to figure out
# the maximum inflation increase from the values the user entered




def main():
    # Set a variable to calculate the max increase in the inflation rate
    max_increase = None
    # Let's set a counter variable to count every user input, starting from 1
    counter = 1
    # We will store every user input in a list for further calculations
    values = []
    # Start a while-loop to start asking the user input until the user enters an empty line
    while True:
        # Ask for the month's inflation rate input
        user_input = input(f"Enter inflation rate for month {counter}: ")
        # Increase the counter for the next month
        counter += 1
        # Set the condition in order to break the loop
        if user_input == "":
            break
        # Add the entries to the value list
        values.append(float(user_input))
    if len(values) < 2:
        print("Error: at least 2 monthly inflation rates must be entered.")
    else:
        # Set a for-loop to calculate the maximum inflation increase within the user inputs
        for i in range(1, len(values)):
            # Deduct every user input by its predecessor
            increase = values[i] - values[i - 1]
            # Set the condition that stores the max increase in the max_increase variable
            if max_increase is None or increase > max_increase:
                max_increase = increase
            elif increase < 0 and (max_increase is None or increase > max_increase):
                max_increase = increase
        print(f"Maximum inflation rate change was {max_increase:.1f} points.")


if __name__ == "__main__":
    main()

