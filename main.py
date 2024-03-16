def main():
    # Specify the book to open
    path_to_file = "books/frankenstein.txt"
    file_contents = print_book(path_to_file)

    # Call the word_count() function
    count = word_count(file_contents)
    
    # Call the character_count() funtion
    char = character_count(file_contents)

    # Call the report() function
    formatted_report = report(char)
    
    # Print the report results
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There were {count} words found in the book\n")

    for reports in formatted_report:
        for key, value in reports.items():
            print(f"The character {key} was found {value} times")
    
    print("--- End report ---")
    
def print_book(book):
    # Open the specified file and print out the contents
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def word_count(file):
    # Seperate each individual word in the book
    words = file.split()
    
    # Count the amount of words in the book
    count = len(words)
    return count

def character_count(document):
    # Make all letters lowercase
    lowered_document = document.lower()
    
    # Create a dictionary to hold letter and occurence count
    characters = {}

    # Populate the dictionary by counting letters only
    for char in lowered_document:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def report(unformatted_text):
    # Sort the dictionary by highest value
    sorted_list = dict(sorted(unformatted_text.items(), key=lambda x: x[1], reverse=True))

    # Convert the original dictionary to a list of dictionaries
    char_list = [{key: value} for key, value in sorted_list.items()]
    return char_list

main()
