"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash_table = {}
        def dfs(node):
            if node in hash_table:
                return hash_table[node]
            copy=Node(node.val)
            hash_table[node]=copy
            for node in node.neighbors:
                copy.neighbors.append(dfs(node))
        return dfs(node) if node is not None else []
            