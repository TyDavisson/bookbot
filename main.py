def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_words(text)
    letters_dict = get_letters_dict(text)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words")
    print()
    get_report(letters_dict)
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_words(text):
    words = text.split()
    return len(words)

def get_letters_dict(text):
    letters_dict = {}
    for c in text:
        lower = c.lower()
        if lower in letters_dict:
            letters_dict[lower] += 1
        else:
            letters_dict[lower] = 1
    return letters_dict
  
def sort_on(dict):
    return dict["num"]
    
def get_report(dict):
    report = []
    for letter in dict:
        if letter.isalpha():
            report.append({"letter": letter, "num": dict[letter]})
    report.sort(reverse=True, key=sort_on)
    for line in report:
        print(f"Letter: {line['letter']}, Count: {line["num"]}")
          
main()