from test_framework import generic_test


def n_queens(n):
    def solve_nqueen_for_row(row):
        if row == n and len(pos) == n:
            result.append(list(list(zip(*pos))[1]))

        for col in range(n):
            def is_safe():
                for cell in pos:
                    if row == cell[0] or col == cell[1] or row-col == cell[0]-cell[1] or row+col == cell[0]+cell[1]:
                        return False
                return True

            if is_safe():
                pos.append((row, col))
                solve_nqueen_for_row(row + 1)
                pos.pop()

    pos = []
    result = []
    solve_nqueen_for_row(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
