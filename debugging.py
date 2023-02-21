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


# def divide(a: int, b: int):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("You cannot divide by zero.")
#     except TypeError:
#         print("Both inputs must be integers or floats.")
#     else:
#         print(f"{result}")

def divide(a: int, b: int):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as error:
        print("Something went wrong.")
        print(error)
    else:
        print(f"{result}")

divide(1,2)
divide(1,0)
divide("a",2)