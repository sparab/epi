from test_framework import generic_test


def is_symmetric(tree):
    def is_symmetric(left, right):
        if not left and not right:
            return True
        elif not left or not right or left.data != right.data:
            return False

        return is_symmetric(left.right, right.left) and is_symmetric(left.left, right.right)

    if not tree:
        return True
    return is_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
