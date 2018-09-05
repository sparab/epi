from test_framework import generic_test


def search_first_of_k(A, k):

    l, h, result= 0, len(A) - 1, -1

    while l <= h:
        mid = (l+h) // 2

        if A[mid] == k:
            result = mid

        if A[mid] >= k:
            h = mid - 1
        else:
            l = mid + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
