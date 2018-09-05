from test_framework import generic_test


def is_balanced_binary_tree(tree):

    def check_balanced(tree):
        if tree is None:
            return 0, True

        left = check_balanced(tree.left)
        right = check_balanced(tree.right)

        if left[1] == right[1] == True and abs(left[0]-right[0]) <= 1:
            return max(left[0], right[0]) + 1, True
        else:
            return max(left[0], right[0]) + 1, False

    return check_balanced(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
