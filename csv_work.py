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