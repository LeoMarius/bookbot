def main():
    book_path = "books/frankenstein.txt"
    # book_text = get_book_text(book_path)
    # print(book_text)
    # num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")

    # letter_count = count_char(book_text)
    # print(letter_count)
    print_report(book_path)

def count_char(text):
    count ={}

    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter in count :
                count[letter]+=1
            else :
                count[letter]=1
    return dict(sorted(count.items()))

def print_report(book_path):

    print(f"--- Begin report of {book_path} ---")

    book_text = get_book_text(book_path)
    num_words = count_words(book_text)

    print(f"{num_words} words found in the document")

    print("")

    letters_count = count_char(book_text)

    for letter in letters_count:
        # print(letter)
        print(f"The '{letter}' character was found '{letters_count[letter]}' times")
    
    print("--- End report ---")

def get_book_text(book):
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def count_words(book_string):
    return len(book_string.split())


main()