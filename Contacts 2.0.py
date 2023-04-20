"""
COMP.CS.100 Programming 1:  9.7: Contacts

Name: Reyver Serna
Email: rs412764@tuni.com
Student Number: 412764
"""
def read_file(file_name):
    """ This is a function that reads a designated csv file to turn into an
    esay-to-look-up data structure
    Paramenters: file_name: str, csv file containing people and contact info
    Returns:data: dict, datastructure for people and contact infor
    """
    contacts = {}
    with open(file_name, 'r') as f:
        header = f.readline().strip().split(';')
        for line in f:
            data = line.strip().split(';')
            contact = {}
            for i, value in enumerate(data):
                contact[header[i]] = value
            key = data[0]
            contacts[key] = contact
    return contacts