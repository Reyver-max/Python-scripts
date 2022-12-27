"""
COMPCS 100 Programming 1. 2.8.3 All Fridays in 2014
Reyver Serna : rs412764@tuni.fi
Student number: 412764
"""
def main():
    # Define the number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Define the names of the months
    month_names = ["1", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "11",
                   "12"]

    # Set the current day, month, and day of the week to the first day of the year
    day = 1
    month = 0
    day_of_week = 2  # 0 = Monday, 1 = Tuesday, etc.

    # Iterate over each day of the year
    for i in range(365):
        # Check if the day is a Friday
        if day_of_week == 4:
            # If it is, print the date in the format "Month Day, Year"
            print(f"{str(day)}.{month_names[month]}.")

        # Increment the day and day of the week
        day += 1
        day_of_week = (day_of_week + 1) % 7

        # Check if the day is the last day of the month
        if day > days_in_month[month]:
            # If it is, reset the day to 1 and increment the month
            day = 1
            month += 1
if __name__ == "__main__":
    main()