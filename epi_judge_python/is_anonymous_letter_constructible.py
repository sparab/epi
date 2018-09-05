from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    d = {}
    for c in letter_text:
        d[c] = d.get(c, 0) + 1

    for c in magazine_text:
        if d.get(c):
            if d[c] == 1:
                del d[c]
                if not d:
                    return True
            else:
                d[c] -= 1

    return not d


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
