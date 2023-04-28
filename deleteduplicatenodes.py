import ast
in_list=ast.literal_eval(input())
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
in_node=ListNode(val=in_list[0])
cur_node=in_node
for i in in_list[1:]:
    cur_node.next=ListNode(val=i)
    cur_node=cur_node.next
def deldupes(in_node):
    if in_node is None:
        return None
    result=in_node
    L_node=result
    R_node=result.next
    while L_node.next is not None:
        if L_node.val==R_node.val:
            R_node=R_node.next
            L_node.next=R_node
        else:
            L_node=L_node.next
            R_node=R_node.next
    return result
result=deldupes(in_node)
cur_node=result
result_list=[]
result_list.append(cur_node.val)
while cur_node.next is not None:
    cur_node=cur_node.next
    result_list.append(cur_node.val)
print(result_list)