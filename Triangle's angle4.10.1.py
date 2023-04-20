"""""
COMP.CS.100. Programming 1. 4.10.1
Reyver Serna: rs412764@tuni.filte
Student number: 412764
"""""

def calculate_angle(angle1, angle2=None):
    """This is a function that calculates the triangle's angle."""
    """it has a, b  as integers parameters. These are float numbers"""
    if angle2 is None:
        # Calculate the other sharp angle in case of a right-angled triangle
        return 90 - angle1
    else:
        # Calculate the third angle of a non-right-angled triangle
        return 180 - angle1 - angle2