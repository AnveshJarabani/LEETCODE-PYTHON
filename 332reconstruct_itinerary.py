from typing import List,DefaultDict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=DefaultDict(list)
        for src,des in sorted(tickets,reverse=True):
            graph[src].append(des)
        itinerary=[]
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs('JFK')
        return itinerary[::-1]