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
    """This function reads users from a CSV file."""
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        list(print(f"{row['First Name']} {row['Last Name']}") for row in csv_reader)


'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
def find_user(first_name: str, last_name: str):
    """This function finds a user based on first and last name."""
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."
    

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
def update_users(old_first: str, old_last: str, new_first: str, new_last: str) -> str:
    """"This function updates a users first and last name."""
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows: list = list(csv_reader)
 
    count: int = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users updated: {count}."


'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(first_name: str, last_name: str) -> str:
    """This function can delete a user based on name."""
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows: list = list(csv_reader)
 
    count: int = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users deleted: {count}."