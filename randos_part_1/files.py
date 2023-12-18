def copy(file_name: str, new_file_name: str) -> None:
    """This function copies the contents of the first file and writes them into the second file."""
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)


def copy_and_reverse(file_name: str, new_file_name: str) -> None:
    """This function copies the contents of the first file and writes them into the second file in reverse."""
    with open(file_name) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])


def statistics(file_name: str) -> dict:
    """This function parses the contents of a file and returns a dictionary of statistics regarding the file."""
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }


def find_and_replace(file_name: str, old_word: str, new_word: str):
    """This function parses the contents of a file and replaces all instances of the old word in the file."""
    with open(file_name, "r+") as file:
        text: str = file.read()
        new_text: str = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()