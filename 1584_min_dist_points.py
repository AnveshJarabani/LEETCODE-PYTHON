from typing import List
from heapq import heappush,heappop
def dst(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=[False]*n
        heap_dct={0:0}
        min_heap=[(0,0)]
        mst_w=0
        while min_heap:
            w,u=heappop(min_heap)
            if visited[u] or heap_dct.get(u,float('inf'))<w:
                continue
            visited[u]=True
            mst_w+=w
            for v in range(n):
                if not visited[v]:
                    new_d=dst(points[u],points[v])
                    if new_d<heap_dct.get(v,float('inf')):
                        heap_dct[v]=new_d
                        heappush(min_heap,(new_d,v))
        return mst_w
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))
"""
Prim's Algorithm Explained
What is Prim's Algorithm?
Prim's Algorithm is another method for finding the Minimum Spanning Tree. It starts from an arbitrary node and greedily chooses the edge with the smallest weight that connects a visited and an unvisited node.

The Mechanics of Prim's Algorithm in "Min Cost to Connect All Points"
Initialize Priority Queue:

Start from an arbitrary point and initialize a minimum priority queue with its edges.
Visited Nodes Tracking:

Keep track of visited nodes to ensure that each node is visited exactly once.
Iterate and Add to MST:

Pop the edge with the smallest weight from the priority queue. If the edge leads to an unvisited node, add the edge's weight to the total MST weight, and insert all edges from that node into the priority queue.
Completion Check:

Continue this process until all nodes have been visited.
Time and Space Complexity
Time Complexity: O(n2log⁡n)O(n^2 \log n)O(n 
2
 logn), due to priority queue operations.
Space Complexity: O(n)O(n)O(n), for storing the priority queue and visited nodes.

"""