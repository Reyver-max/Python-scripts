"""
COMP.CS.100 Programming 1. 10.10 Scoring for Mölkky

Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rounds_played = 0
        self.successful_scores = 0

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, points):
        if points < 0:
            print(self.name + " gets penalty points!")
        self.points += points
        if self.points > 50:
            self.points = 25
            print(self.name + "'s score has been dropped to 25 points.")
        elif 40 <= self.points <= 49:
            self.print_warning()
        self.rounds_played += 1
        if points > 0:
            self.successful_scores += 1
            if points > self.get_average_points():
                self.print_cheers()

    def has_won(self):
        return self.points >= 50

    def print_warning(self):
        missing_points = 50 - self.points
        print(self.name + " needs only " + str(missing_points) +
              " points. It's better to avoid knocking down the pins with higher points.")

    def print_cheers(self):
        print("Cheers " + self.name + "!")

    def get_average_points(self):
        return self.points / self.rounds_played if self.rounds_played > 0 else 0

    def get_success_percentage(self):
        if self.rounds_played > 0:
            return (self.successful_scores / self.rounds_played) * 100
        else:
            return 0


def main():
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage",
              format(player1.get_success_percentage(), ".1f"))
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage",
              format(player2.get_success_percentage(), ".1f"))
        print("")

        throw += 1


if __name__ == "__main__":
    main()





