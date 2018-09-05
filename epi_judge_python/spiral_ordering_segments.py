from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    def traverse_layer_clockewise(offset):
        traverse_length = len(square_matrix) - offset - 1
        if offset == traverse_length:
            result.append(square_matrix[offset][offset])
            return

        i = j = offset
        counter = offset
        while counter < traverse_length:
            result.append(square_matrix[i][j])
            counter, j = counter+1, j+1

        counter = offset
        while counter < traverse_length:
            result.append(square_matrix[i][j])
            counter, i = counter+1, i+1

        counter = offset
        while counter < traverse_length:
            result.append(square_matrix[i][j])
            counter, j = counter+1, j-1

        counter = offset
        while counter < traverse_length:
            result.append(square_matrix[i][j])
            counter, i = counter+1, i-1

    result = []
    for k in range(len(square_matrix)+1 // 2):
        traverse_layer_clockewise(k)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
