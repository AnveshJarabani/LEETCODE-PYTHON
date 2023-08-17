from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n_lst=[i for i in range(1,n+1)]
        def dfs(inp_lst,path):
            if len(path)==k:
                result.append(path[:])
                return
            for i in range(len(inp_lst)):
                path.append(inp_lst[i])
                dfs(inp_lst[i+1:],path)
                path.pop()
        result=[]
        dfs(n_lst,[])
        return result
print(Solution().combine(n=4,k=2))