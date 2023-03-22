def copy(file_name: str, new_file_name: str) -> None:
    """This function copies the contents of the first file and writes them into the second file."""
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)