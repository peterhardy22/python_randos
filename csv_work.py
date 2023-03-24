import csv

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
def add_user(first_name: str, last_name: str) -> None:
    """This function takes in a first and last name, then writes it into the users.csv file."""
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])


'''
print_users() # None
# prints to the console:
# Colt Steele
'''
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        list(print(f"{row['First Name']} {row['Last Name']}") for row in csv_reader)


'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
def find_user(first_name: str, last_name: str):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."