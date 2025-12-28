import sys
from stats import book_analyzer
from stats import count_characters
from stats import sort_dict
from stats import sum_of_letters

num_words = book_analyzer("num words") # number of words in the supplied .txt
num_characters = count_characters() # character dictionary and count of each item
contents = book_analyzer("words") # plain text of the supplied .txt
report = sort_dict() # sorted list of dictionaries with character and count
book = ""

if len(sys.argv) < 2 and ".txt" not in sys.argv[0]:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
elif ".txt" in sys.argv[0]:
        book = sys.argv[0]
else: book = sys.argv[1]

def main():
    write_report()

def strip_file_location(book):
    # return file name only, strip out anything before "/"
    for words in book.split("/"):
        if ".txt" in words:
            return words

def write_report():
    # create a txt document named report.txt and capture the results within
    book_name = strip_file_location(book)
    total_letters = sum_of_letters()
    message = (
        f"*** Beginning analysis of {book_name} ***\n\n"
        "===== Word Count =====\n"
        f"Found {num_words} total words!\n\n"
        "===== Character Count =====\n"
    )
    # for loop to append each letter and its count to the message
    for data in report:
        message += str(data["char"]) + ": " + str(data["num"]) + "\n"

    message += (
        f"That's a total of {total_letters} letters in the book!\n\n"
        "Thank you for using BookBot!\n\n"
        "*** End of analysis ***"
    )
    with open("report.txt", "w") as f:
        print(message, file=f)
    return print(message)

main()