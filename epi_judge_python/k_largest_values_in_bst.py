from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    def find_largest_helper(root, k):
        if not root:
            return k

        if k > 0:
            k = find_largest_helper(root.right, k)
        if k > 0:
            result.append(root.data)
            k -= 1
        if k > 0:
            k = find_largest_helper(root.left, k)

        return k

    result = []
    find_largest_helper(tree, k)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
