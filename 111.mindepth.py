
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def height(self,root,cur_depth=0):
            if not root:
                return 
            if root.left and root.right:
                self.min_depth=min(self.min_depth,cur_depth+1)
            self.height(root.left,cur_depth+1)
            self.height(root.right,cur_depth+1)
        if not root:
            return 0
        self.min_depth=float('inf')
        self.height(root)
        return self.min_depth