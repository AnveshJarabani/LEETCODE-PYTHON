
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[root.val]
        result+=self.preorderTraversal(root.left)
        result+=self.preorderTraversal(root.right)
        return result
        
