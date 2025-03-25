import sys
from stats import get_word_count, get_char_count, sort_char_dict

def get_book_text(fp):
    with open(fp, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    num_char = get_char_count(book_text)
    sorted_chars = sort_char_dict(get_char_count(book_text))

    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
    """)
    for s in sorted_chars:
        print(f"{s["char"]}: {s["count"]}")
main()