from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    rows = [set() for _ in range(len(partial_assignment))]
    columns = [set() for _ in range(len(partial_assignment))]
    squares = [set() for _ in range(len(partial_assignment))]

    for i in range(len(partial_assignment)):
        for j in range(len(partial_assignment)):
            num = partial_assignment[i][j]

            if num:
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)

                if num in columns[j]:
                    return False
                else:
                    columns[j].add(num)

                def get_square_index():
                    i_index, j_index = 0, 0
                    if i in range(0, 3):
                        i_index = 0
                    elif i in range(3, 6):
                        i_index = 3
                    else:
                        i_index = 6

                    if j in range(0, 3):
                        j_index = 0
                    elif j in range(3, 6):
                        j_index = 1
                    else:
                        j_index = 2

                    return i_index + j_index

                square_index = get_square_index()

                if num in squares[square_index]:
                    return False
                else:
                    squares[square_index].add(num)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
