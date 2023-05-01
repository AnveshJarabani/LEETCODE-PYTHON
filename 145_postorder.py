
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=self.postorderTraversal(root.left)
        result+=self.postorderTraversal(root.right)
        result.append(root.val)
        return result