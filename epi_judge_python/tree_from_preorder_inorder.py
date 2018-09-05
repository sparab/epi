from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
    if len(preorder) == len(inorder) == 1:
        return BinaryTreeNode(preorder[0])
    elif not preorder and not inorder:
        return None

    mid = inorder.index(preorder[0])
    new_node = BinaryTreeNode(preorder[0],
                              binary_tree_from_preorder_inorder(preorder[1:mid+1], inorder[:mid]),
                              binary_tree_from_preorder_inorder(preorder[mid+1:], inorder[mid+1:]))

    return new_node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
