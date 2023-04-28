import ast
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if root is None:
        return []
    cur=root
    result=[cur.val]
    while cur is not None:
        if cur.right is not None:
            result.append(cur.right.val)
            cur=cur.right
        else:
            if cur.left is not None:
                result.append(cur.left.val)
                cur=cur.left
            else:
                return result
in_list=ast.literal_eval(input())
in_root=TreeNode(val=in_list[0])
cur_node=in_root
for x,i in enumerate(in_list[1:]):
    if i is not None:
        cur_node.left=TreeNode(val=i)
        cur_node=cur_node.left
    else:
        cur_node.right=in_list[x+1]
        continue
print(inorderTraversal(in_root))