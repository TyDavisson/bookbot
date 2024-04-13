def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_words(text)
    num_letters = get_letters(text)
    print(f"{num_words} words")
    print(num_letters)

def get_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    for c in text:
        lower = c.lower()
        if lower in letters:
            letters[lower] += 1
        else:
            letters[lower] = 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def report(dict):
    
    
main()