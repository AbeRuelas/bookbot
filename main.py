def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_chars = count_characters(text)
    list_dicts = convert_dict(count_chars)
    sorted_lists = sort_on(list_dicts)
    
    print(f"-- Begin report of {book_path} --")
    print(f"{num_words} words found in the document")
    print()
    
    for item in sorted_lists:
        if not item['char'].isalpha():
            continue
        print(f"The' {item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def convert_dict(count_chars):
    return [{'char':key,'num':value} for key, value in count_chars.items()]

def sort_by_num(d):
    return d['num']

def sort_on(list_dicts):
    list_dicts.sort(reverse=True, key=sort_by_num)
    return list_dicts
    

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
