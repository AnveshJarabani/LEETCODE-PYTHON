# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        return_list1 = []
        return_list2 = []

        def leaf(root, arr):
            if root:
                leaf(root.left, arr)
                if root.left is None and root.right is None:
                    arr.append(root.val)
                leaf(root.right, arr)

        leaf(root1, return_list1)
        leaf(root2, return_list2)
        return return_list1 == return_list2
