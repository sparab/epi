from test_framework import generic_test


def find_nearest_repetition(paragraph):
    d, least_distance = {}, float('inf')

    for i, word in enumerate(paragraph):
        if word in d:
            least_distance = min(i - d[word], least_distance)
        d[word] = i

    return least_distance if least_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
