def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_chars = count_characters(text)
    print(count_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
 
def count_characters(text_file):
    charDict = {}

    for c in text_file:
        if c.isalpha():
            low_c = c.lower()
            if low_c in charDict:
                charDict[low_c] += 1
            else:
                charDict[low_c] = 1
    return charDict        
main()

