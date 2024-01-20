def main():
    book_path = "books/"
    book_name = "frankenstein.txt"
    book = book_path + book_name
    words = read_book(book)
    num_words = count_words(words)
    num_characters = count_characters(words)
    num_letters = book_report(num_characters)
    with open("books/report.txt", "a") as f:
        print(f"That's a total of {"{:,}".format(num_letters[1])} letters!\n*** This is the end of the {book_name} report! ***", file=f)
        

def read_book(book):
    with open(book) as file:
        return file.read()
    
def count_words(words):
    numbers = words.split()
    with open("books/report.txt", "w") as f:
        print(f"*** Beginning report of frankenstein.txt, hold tight! ***", file=f)
        print(f"{"{:,}".format(len(numbers))} words found in frakenstein.txt!", file=f)
    return len(numbers)

def count_characters(words):
    duplicates = {}
    for letters in words.lower():
        if letters in duplicates:
            duplicates[letters] += 1
        else: duplicates[letters] = 1
    return duplicates

def book_report(num_characters):
    num_letters = {}
    alphabet = []
    total = 0
    for characters in num_characters:
        if characters.isalpha() == True:
            alphabet.append(characters)
            alphabet.sort()
    for letters in alphabet:
        num_letters[letters] = num_characters[letters]
        with open("books/report.txt", "a") as f:
            print(f"The '{letters}' character was found in frankenstein.txt {num_letters[letters]} times!", file=f)
    for i in num_letters.values():
        total += i
    return num_letters, total
main()
