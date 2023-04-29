import ast
import bigtree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res


class solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        def inord(root):
            if root is None:
                return
            stack.append(root.val)
            inord(root.left)
            res.append(stack.pop(-1))
            inord(root.right)
        inord(root)
        return res
in_list=ast.literal_eval(input())
root=TreeNode(val=in_list[0])
cur_node=root
for x,i in enumerate(in_list[1:]):
    if i is not None:
        cur_node.left=TreeNode(val=i)
        cur_node=cur_node.left
    else:
        cur_node.right=in_list[x+1]
        continue
print(inorderTraversal(root))