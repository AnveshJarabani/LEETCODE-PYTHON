class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack,res=[-1],0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                res=max(res,i-stack[-1])
        return res
Solution().longestValidParentheses(")))()(()")