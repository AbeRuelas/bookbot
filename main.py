def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    word_count = len(words)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

