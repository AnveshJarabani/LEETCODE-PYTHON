from typing import List, Optional


# merge k sorted --
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def merge(lst1, lst2):
            dummy = ListNode()
            cur_node = dummy
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    cur_node.next = lst1
                    lst1, cur_node = lst1.next, cur_node.next
                else:
                    cur_node.next = lst2
                    lst2, cur_node = lst2.next, cur_node.next
            if lst1:
                cur_node.next = lst1
            else:
                cur_node.next = lst2
            return dummy.next

        result = lists[0]
        for i in lists[1:]:
            result = merge(result, i)
        return result


# combination sum
class Solution:
    def combinationSum(self, lst: List[int], target: int) -> List[List[int]]:
        def back_tracker(i=0, cur=[], sum=0):
            if sum == target:
                result.append(cur[:])
                return
            elif sum > target or i >= len(lst):
                return
            cur.append(lst[i])
            back_tracker(i, cur, sum + lst[i])
            cur.pop()
            back_tracker(i + 1, cur, sum)

        result = []
        back_tracker()
        return result


# 53 maximum_subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = nums[0], 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            res = max(res, cur)
        return res


# 54 spiral matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            if matrix:
                for each_row in matrix:
                    if each_row:
                        result.append(each_row.pop(-1))
            if matrix:
                last_row = matrix.pop(-1)
                result.extend(last_row[::-1])
            if matrix:
                for each_row in matrix[::-1]:
                    if each_row:
                        result.append(each_row.pop(0))
        return result


# 62 unique paths :
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def bt(down=1, right=1):
            if down > m or right > n:
                return 0
            elif down == m and right == n:
                return 1
            return bt(down + 1, right) + bt(down, right + 1)

        return bt()


# 11 container with most water
class Solution:
    def maxArea(self, lst: List[int]) -> int:
        l, r = 0, len(lst) - 1
        vol = 0
        while l < r:
            vol = max(vol, min(lst[r], lst[l]) * (r - l))
            if lst[l] < lst[r]:
                l += 1
            else:
                r -= 1
        return vol


# 63_ UNIQUE PATHS 2
class Solution:
    def uniquePathsWithObstacles(self, lst: List[List[int]]) -> int:
        depth, width = len(lst), len(lst[0])

        @cache
        def bt(down=1, right=1):
            if (down > depth or right > width) or lst[down - 1][right - 1]:
                return 0
            elif down == depth and right == width:
                return 1
            return bt(down + 1, right) + bt(down, right + 1)

        return bt()


# 79 word search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def rec(x, y, i):
            if i == len(word):
                return True
            if (
                x < 0
                or y < 0
                or x > n - 1
                or y > m - 1
                or board[x][y] != word[i]
                or (x, y) in path
            ):
                return False
            path.add((x, y))
            res = (
                rec(x + 1, y, i + 1)
                or rec(x - 1, y, i + 1)
                or rec(x, y + 1, i + 1)
                or rec(x, y - 1, i + 1)
            )
            # path.remove((x,y))
            return res

        for x in range(n):
            for y in range(m):
                if rec(x, y, 0):
                    return True
        return False


# 98.validate binary sarch tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def bt(node):
            nonlocal prev
            if not node:
                return True
            if not (bt(node.left) and prev < node.val):
                return False
            prev = node.val
            return bt(node.right)

        return bt(root)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, val, path):
            if not node:
                return
            val -= node.val
            path.append(node.val)
            if not node.right and not node.left and val == 0:
                res.append(path[:])
            dfs(node.left, val, path)
            dfs(node.right, val, path)
            path.pop()

        dfs(root, targetSum, [])
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 0
        for i in nums:
            if i - 1 not in numset:
                lgth = 0
                while i + lgth in numset:
                    lgth += 1
                result = max(lgth, result)
        return result


# 238 product except self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# 240 matrix 2d search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, m = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while r >= 0 and c < m:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False


# return first unique character


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_set = {}
        for i in s:
            if i in char_set:
                char_set[i] = False
            else:
                char_set[i] = True
        for i, val in enumerate(s):
            if char_set[val]:
                return i
        return -1


# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        result = [0] * len(t)
        stack = []  # keyparr[i,val]
        for i, val in enumerate(t):
            while stack and val > stack[-1][1]:
                stack_i, stack_val = stack.pop()
                result[stack_i] = i - stack_i
            stack.append([i, val])
        return result
