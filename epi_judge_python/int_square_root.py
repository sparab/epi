from test_framework import generic_test


def square_root(k):
    result, lower, higher = -1, 0, k

    while lower <= higher:
        mid = (lower + higher) // 2
        if mid ** 2 == k:
            return mid
        elif mid ** 2 < k:
            result = mid
            lower = mid + 1
        else:
            higher = mid - 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
