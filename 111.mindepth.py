class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que=[]
        d=1
        que.append((root,d))
        while que:
            cur,d=que.pop(0)
            if not cur.left and not cur.right:
                return d
            if cur.left:
                que.append((cur.left,d+1))
            if cur.right:
                que.append((cur.right,d+1))
        return d