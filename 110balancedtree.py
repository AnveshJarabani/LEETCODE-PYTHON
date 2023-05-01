
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def validate(root):
            if not root: return [True,0]
            left_bal, right_bal=validate(root.left), validate(root.right)
            balanced=(left_bal[0] and right_bal[0] and abs(left_bal[1]-right_bal[1])<2)
            return [balanced,1+max(left_bal[1],right_bal[1])]
        return validate(root)[0]