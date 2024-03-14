def main():
    # specify the book to open
    path_to_file = "books/frankenstein.txt"
    file_contents = print_book(path_to_file)

    # call the word_count() function
    count = word_count(file_contents)
    
    # call the character_count() funtion
    char = character_count(file_contents)
    print(char)
    
def print_book(book):
    # open the specified file and prints out the contents
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def word_count(file):
    # seperate each individual word in the book
    words = file.split()
    
    # count the amount of words in the file_contents
    count = len(words)
    return count

def character_count(document):
    # make all letters lowercase
    lowered_document = document.lower()
    
    # create a dictionary to hold each character and count
    characters = {}

    # populate the dictionary by counting characters
    for char in lowered_document:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

main()
