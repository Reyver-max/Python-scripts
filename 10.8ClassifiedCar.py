"""
COMP.CS.100 Programming 1. 10.8  Classified Car

Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0
        self.__odometer = 0

    def print_information(self):
        """
        Prints the amount of gas in the car's tank and the number
        of kilometers shown on the car's odometer.
        """
        print(f"The tank contains {self.__gas:.1f} liters of gas and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, amount):
        """
        Refuels the car's tank with the specified amount of gas.

        :param amount: float, the amount of gas to fill the tank with
        """

        if amount < 0:
            print("You cannot remove gas from the tank")
        else:
            available_space = self.__tank_volume - self.__gas
            if amount <= available_space:
                self.__gas += amount
            else:
                self.__gas = self.__tank_volume

    def drive(self, distance):
        """
        Drives the car for the specified distance.

        :param distance: float, the distance in kilometers to drive
        """

        if distance < 0:
            print("You cannot travel a negative distance.")
        else:
            max_distance = (self.__gas / self.__consumption) * 100
            if distance < max_distance:
                self.__odometer += distance
                self.__gas -= (distance / 100) * self.__consumption
            else:
                self.__odometer += max_distance
                self.__gas = 0


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
