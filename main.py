from stats import get_word_count

def get_book_text(fp):
    with open(fp, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    get_word_count(get_book_text("books/frankenstein.txt"))
