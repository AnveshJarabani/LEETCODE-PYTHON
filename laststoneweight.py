import ast
lst=ast.literal_eval(input())
class Solution:
    def laststoneweight(self,stones) -> int:
        stones.sort(reverse=True)
        while (len(stones)>1):
            x=stones.pop(0)
            y=stones.pop(0)
            if x!=y:
                stones.append(abs(x-y))
                stones.sort(reverse=True)
        return stones[0] if stones else 0
print(Solution().laststoneweight(stones=lst))

            

            


