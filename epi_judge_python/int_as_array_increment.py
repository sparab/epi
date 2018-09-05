from test_framework import generic_test


def plus_one(A):
    carry = 0
    if A[-1] is not 9:
        A[-1] += 1
        return A

    for i in range(len(A) - 1, -1, -1):
        if A[i] == 9:
            A[i] = 0
            carry = 1
        else:
            A[i] += carry
            carry = 0

        if carry == 0:
            break

    if carry:
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
