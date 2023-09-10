# def tree_build(self,lst):
#     if not lst:
#       return Node()
def get_cheapest_cost(root):
    def rec(node):
        if not node:
            return 0
        if not node.children:
            return node.cost
        min_val = float("inf")
        for i in node.children:
            min_val = min(rec(i), min_val)
            print(i.cost)
        return min_val + node.cost

    return rec(root)


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost=None, children=[], parent=None):
        self.cost = cost
        self.children = children
        self.parent = parent


root = Node(
    0,
    children=[
        Node(5, children=[Node(4)]),
        Node(3, children=[Node(2), Node(1)]),
        Node(6, children=[Node(1), Node(5)]),
    ],
)


# lst = [0,5,3,6,4,None,2,0,1,5,None,None,1,None,10,None,None,None,None,None,None,1]
print(get_cheapest_cost(root))
