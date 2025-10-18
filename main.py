#!/usr/bin/env python3

import sys
from stats import count_words, each_character_count, sort_character_count_list


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[2:]}...")  # Remove "./" prefix

    # Get book text
    text = get_book_text(book_path)

    # Word count section
    print("----------- Word Count ----------")
    print(count_words(text))

    # Character count section
    print("--------- Character Count -------")
    char_count = each_character_count(text)
    sorted_chars = sort_character_count_list(char_count)

    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['num']}")

    print("============= END ===============")


main()
