# find_and_replace

def find_and_replace(file_name, word_search, word_replace):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(word_search, word_replace)
        file.seek(0)
        file.write(new_text)
        file.truncate()


find_and_replace("story2.txt", "Alice", "Colt")


