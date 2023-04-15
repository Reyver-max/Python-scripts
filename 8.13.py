""""                                                                          
COMPCS100. Programming 1. 8.13 Calculating scores                             
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
            for line_num, line in enumerate(f, start=1):
                # Split line into player name and score
                parts = line.strip().split()
                if len(parts) != 2:
                    print(f"There was an erroneous line in the file:")
                    print(line.strip())
                    break
                name, score_str = parts
                try:
                    score = int(score_str)
                except ValueError:
                    print(f"There was an erroneous score in the file:")
                    print(score_str)
                    break
                # Add score to player's total score
                if name in player_scores:
                    player_scores[name] += score
                else:
                    player_scores[name] = score
    except OSError:
        print("There was an error in reading the file.")




if __name__ == "__main__":
    main()
"""        # Print scores for all players in alphabetical order
    if player_scores:
        print("Total scores:")
        for name in sorted(player_scores.keys()):
            print(f"{name}: {player_scores[name]}")"""