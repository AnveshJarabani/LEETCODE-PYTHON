import ast
import bigtree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res=[]
    def inord(root):
        if root is None:
            return
        inord(root.left)
        res.append(root.val)
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