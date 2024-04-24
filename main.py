def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words(text)
    letter_counts = get_letters(text)
    print_report(book_path, word_count, letter_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    text_lower = text.lower()
    d_letters = {}

    for letter in text_lower:
        if letter in d_letters:
            d_letters[letter] += 1
        else:
            d_letters[letter] = 1
    return d_letters

def print_report(path, words, letters):
    letter_list = []
    for letter in letters:
        if letter.isalpha():
            temp_dic = {"letter":letter, "count": letters[letter]}
            letter_list.append(temp_dic)
    letter_list.sort(key=sort_on, reverse=True)

    print(f"<--- Begin report of {path} --->")
    print(f"{words} words were found in the document")
    print()
    for i in range(0, len(letter_list)):
        print(f"The {letter_list[i]["letter"]} character was found {letter_list[i]["count"]} times")
    print("<--- End of Report --->")
def sort_on(dict):
    return dict["count"]
    


main()
