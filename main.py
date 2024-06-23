def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    count_chars = count_characters(text)
    print(count_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()
 
def count_characters(text_file):
    charDict = {}

    for c in text_file:
        if c.isalpha():
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
    return charDict        
main()

