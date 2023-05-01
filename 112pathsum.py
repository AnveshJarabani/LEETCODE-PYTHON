
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(root,sm):
            if not root:
                return False
            sm+=root.val
            if not root.left and not root.right:
                return sm==targetSum
            return (pathsum(root.left,sm) or pathsum(root.right,sm))
        return pathsum(root,0)
        

        