#!/usr/bin/env python3


def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"


def each_character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# create sort_character_count function; don't use lambda functions. use simple
# constructs.
def sort_character_count(char_count):
    # Normalize case and merge counts for same letters
    normalized_count = {}
    for char, count in char_count.items():
        lower_char = char.lower()
        if lower_char in normalized_count:
            normalized_count[lower_char] += count
        else:
            normalized_count[lower_char] = count

    # Sort the normalized counts
    sorted_count = {}
    for char in sorted(normalized_count.keys()):
        sorted_count[char] = normalized_count[char]
    return sorted_count


def get_num_key(char_dict):
    """Helper function to return the 'num' key for sorting"""
    return char_dict["num"]


def sort_character_count_list(char_count):
    """Convert character count dict to sorted list of dicts by count (descending)"""
    char_list = []

    # Convert dict to list of dicts, only including alphabetical characters
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    # Sort by count (descending) using helper function
    char_list.sort(key=get_num_key, reverse=True)

    return char_list
