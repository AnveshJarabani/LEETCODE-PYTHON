# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergetrees(r1, r2):
    if r1 is None and r2 is None:
        return None
    val1 = r1.val if r1 else 0
    val2 = r2.val if r2 else 0
    r3 = TreeNode(val1 + val2)
    r3.left = mergetrees(r1.left if r1 else None, r2.left if r2 else None)
    r3.right = mergetrees(r1.right if r1 else None, r2.right if r2 else None)
    return r3
