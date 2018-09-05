from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    i, j = 0, 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if (i == 0 or j == 0) or (A[i-1] != A[i] or B[j-1] != B[j]):
                result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))