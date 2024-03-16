def main():
    # specify the book to open
    path_to_file = "books/frankenstein.txt"
    file_contents = print_book(path_to_file)

    # call the word_count() function
    count = word_count(file_contents)
    
    # call the character_count() funtion
    char = character_count(file_contents)

    # call the report() function
    formatted_report = report(char)
    
    # printing the report results
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There were {count} words found in the book\n")

    for reports in formatted_report:
        for key, value in reports.items():
            print(f"The character {key} was found {value} times")
    
    print("--- End report ---")
    
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

    # populate the dictionary by counting letters
    for char in lowered_document:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def report(unformatted_text):
    # sort the list of dictionaries by highest value
    sorted_list = dict(sorted(unformatted_text.items(), key=lambda x: x[1], reverse=True))

    # convert the original dictionary to a list of dictionaries
    char_list = [{key: value} for key, value in sorted_list.items()]
    return char_list

main()
