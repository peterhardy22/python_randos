# try:
# except:
# else:
# finally:

while True:
    try:
        number: int = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("This is a number!")
        break
    finally:
        print("Runs every time regardless of a break in the else!")