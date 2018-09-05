from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    i, j, k = m-1, n-1, m+n-1

    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i, k = i-1, k-1
        else:
            A[k] = B[j]
            j, k = j-1, k-1

    if i == -1:
        while j >= 0:
            A[k] = B[j]
            j, k = j - 1, k - 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
