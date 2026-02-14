import sys
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

def book_analyzer(x):
    # attempt to open supplied txt, create an error log if not found
    if len(sys.argv) < 2 and ".txt" not in sys.argv[0]:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    elif ".txt" in sys.argv[0]:
        book = sys.argv[0]
    else: book = sys.argv[1]
    try:
        with open(book) as f:
            contents = f.read().lower()
    except FileNotFoundError:
        with open("error.log", "a") as f:
            print(f"[{current_time}] *** Error! {book} not found! ***", file=f)
    if x == "num words":
        # return the number of words in the supplied book
        return len(contents.split())
    if x == "words":
        # return the plain text we opened earlier
        return contents

def count_characters():
    # count each character and increase the count by 1 if it's not unique and then return the dictionary
    duplicates = {}
    for letters in book_analyzer("words"):
        if letters in duplicates:
            duplicates[letters] += 1
        else: duplicates[letters] = 1
    return duplicates

def sort_by_greatest(list):
    # return the num value to sort our results by greatest to smallest
    return list["num"]

def sort_dict():
    # creates a list of dictionaries that contains 2 key, value pairs. The first value being the actual letter, the second value being how many times it appears in the txt.
    num_characters = count_characters()
    sorted_list = []
    alphabet = []
    for characters in num_characters:
        if characters.isalpha() == True:
            alphabet.append(characters)
    for letters in alphabet:
        sorted_list.append({"char": letters, "num":num_characters[letters]})
    sorted_list.sort(reverse=True, key=sort_by_greatest)
    return sorted_list

def sum_of_letters():
    # add up all letters and returns a final count
    num_characters = count_characters()
    total = 0
    for characters in num_characters:
        if characters.isalpha() == True:
            total += num_characters[characters]
    return total