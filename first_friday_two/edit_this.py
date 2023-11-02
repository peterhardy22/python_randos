# # open() is a built-in Python function (no imports!)
# # Allows you to open a file and return a corresponding file object.
# # Multiple optional parameters, but the name of the file is mandatory.
# file = open("starter.txt")
# print(file) 
# print(file.read())

# seek
# file = open("starter.txt")
# print(file.read())
# print(file.read())
# file.seek(0)
# print(file.read())

# readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# file.close()

# Use with statement to no longer manually close file
# with open("starter.txt") as file:
#     data = file.read()

# print(data)


# with open("starter.txt", "w") as file:
#     file.write("This is a sentence!\n")
#     file.write("This is our second sentence!!\n")
#     file.write("This is my sentence!!!")

with open("starter.txt", "w") as file:
    file.write("This isn't a question!\n")
    file.write("Why even question it?\n")
    file.write("That was a question!!")