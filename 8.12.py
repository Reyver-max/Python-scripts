""""
COMPCS100. Programming 1. 8.12 Calculating scores
Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""""

def main():
    # Define dictionary to store scores for each player
    player_scores = {}

    # Prompt user for name of score file
    filename = input("Enter the name of the score file: ")

    # Read scores from file
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Split line into player name and score
                name, score_str = line.strip().split()
                score = int(score_str)
                # Add score to player's total score
                if name in player_scores:
                    player_scores[name] += score
                else:
                    player_scores[name] = score
    except OSError:
        print(f"There was an error in reading the file.")
        exit()

    # Print scores for all players in alphabetical order
    if player_scores:
        print("Contestant score:")
        for name in sorted(player_scores.keys()):
            print(f"{name} {player_scores[name]}")
    else:
        print("No scores found in file.")
if __name__ == "__main__":
    main()