#-----------------------------------------------
# 101_symmetrictree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val==right.val and sym(left.right,right.left) and sym(left.left,right.right))
        return sym(root.left,root.right)
#-----------------------------------------------



#-----------------------------------------------
# 104maxdepth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.maxDepth(root.left)+1
        right=self.maxDepth(root.right)+1
        return max(left,right)#-----------------------------------------------



#-----------------------------------------------
# 108heightbalanced
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(self, nums):
    def helper(l,r):
        if l>r:
            return None
        m=(l+r)//2
        root=TreeNode(nums[m])
        root.left=helper(l,m-1)
        root.right=helper(m+1,r)
        return root
    return helper(0,len(nums)-1)#-----------------------------------------------



#-----------------------------------------------
# 110balancedtree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def validate(root):
            if not root: return [True,0]
            left_bal, right_bal=validate(root.left), validate(root.right)
            balanced=(left_bal[0] and right_bal[0] and abs(left_bal[1]-right_bal[1])<2)
            return [balanced,1+max(left_bal[1],right_bal[1])]
        return validate(root)[0]#-----------------------------------------------



#-----------------------------------------------
# 111.mindepth
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
        return d#-----------------------------------------------



#-----------------------------------------------
# 112pathsum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(root,sm):
            if not root:
                return False
            sm+=root.val
            if not root.left and not root.right:
                return sm==targetSum
            return (pathsum(root.left,sm) or pathsum(root.right,sm))
        return pathsum(root,0)
        

        #-----------------------------------------------



#-----------------------------------------------
# 118pascalstriangle
import ast


# def generate(rn):
#     res = [[1]]
#     if rn == 1:
#         return res
#     for i in range(1, rn):
#         res.append(last_lst(res[-1]))
#     return res


# def last_lst(lst):
#     result = [lst[0]]
#     for i in range(0, len(lst)-1):
#         result.append(lst[i]+lst[i+1])
#     result.append(lst[-1])
#     return result
def generate(rn):
    res=[]
    for i in range(rn):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=res[i-1][j-1]+res[i-1][j]
        res.append(row)
    return res

num = ast.literal_eval(input())
print(generate(num))


#-----------------------------------------------



#-----------------------------------------------
# 119pascaltriangle2
# def generate(rn):
#     res = [[1]]
#     if rn == 0:
#         return res
#     for i in range(0, rn):
#         res.append(last_lst(res[-1]))
#     return res[-1]


# def last_lst(lst):
#     result = [lst[0]]
#     for i in range(0, len(lst)-1):
#         result.append(lst[i]+lst[i+1])
#     result.append(lst[-1])
#     return result
import ast

def generate(rn):
    output=[1]
    for i in range(1,rn+1):
        output.append(1)
        for j in range(len(output)-2,0,-1):
            output[j]+=output[j-1]
    return output
rn=ast.literal_eval(input())
print(generate(rn))#-----------------------------------------------



#-----------------------------------------------
# 11_container
class Solution:
    def maxArea(self, lst: List[int]) -> int:
        n=len(lst)
        stack=[]
        for i in range(n-1):
            for j in range(i+1,n):
                stack.append(min(lst[j],lst[i])*(j-i))
        return max(stack)
    
# BIG O(N) - LINEAR TIME COMPLEXITY. 
# JUST MOVE ONE OF THE L OR R POINTERS BASED ON WHICH IS TALLER.
# THIS IS BECAUSE YOU WANT TO CHECK THE POSSIBILITY OF A BIGGER VALUE EXISTING. SO KEEP COMPARING WITH HIGHER VALS.
class Solution:
    def maxArea(self, lst: List[int]) -> int:
        n=len(lst)
        l,r=0,n-1
        max_vol=0
        while l<r:
            max_vol=max(max_vol,(r-l)*min(lst[l],lst[r]))
            if lst[l]<lst[r]:
                l+=1
            else: r-=1
        return max_vol#-----------------------------------------------



#-----------------------------------------------
# 121.besttimeforstock
def maxprofit(lst):
    l,r,maxP=0,1,0
    while r<len(lst):
        if lst[l]<lst[r]:
            cur=lst[r]-lst[l]
            maxP=max(maxP,cur)
        else:
            l=r
        r+=1
    return maxP
import ast
print(maxprofit(ast.literal_eval(input())))

#   profit=0
#         for i in range(0,len(lst)-1):
#             cur_profit=max(lst[i+1:])-min(lst[0:i+1])
#             if cur_profit>profit:
#                 profit=cur_profit
#         return profit#-----------------------------------------------



#-----------------------------------------------
# 122_max_profit_II
"""
FIND THE LARGEST PROFIT POSSIBLE IN A LIST 

in cases like this, 
use two pointers, but the key is to move the lp to the current rp 
because we have already found the max from the past lp to current rp
so this makes the code efficient.

"""
from typing import List
x=[1,2,3]
for i,val in enumerate(x):
    x.pop(i)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp, total_profit = 0, 1, 0
        while rp < len(prices):
            if prices[rp] > prices[lp]:
                total_profit += prices[rp] - prices[lp]
                lp = rp
            else:
                lp = rp
            rp += 1
        return total_profit
#-----------------------------------------------



#-----------------------------------------------
# 125_validpalindrome
def palindrome(s):
    lst=[i for i in s.lower() if i.isalpha()]
    if len(lst)==1:
        return False
    elif len(lst)%2!=0:
        return lst[:len(lst)//2]==lst[(len(lst)//2)+1:][-1::-1]
    else:
        return lst[:len(lst)//2]==lst[len(lst)//2:][-1::-1]
print(palindrome(input()))
#-----------------------------------------------



#-----------------------------------------------
# 133.clone_graph
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
            #-----------------------------------------------



#-----------------------------------------------
# 136_singlenum
import ast
def single(nums):
    res=0
    for n in nums:
        res= n^res
    return res
    
    
    # stack=[]
    # for i in nums:
    #     if i in stack:
    #         stack.remove(i)
    #     else:
    #         stack.append(i)
    # return stack[0]
    
print(single(ast.literal_eval(input())))

#-----------------------------------------------



#-----------------------------------------------
# 139.word_break
def wordbreak(s, dct):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for w in dct:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
                break
    return dp[0]


s = "leetcode"
dct = ["leet", "code"]

print(wordbreak(s, dct))
#-----------------------------------------------



#-----------------------------------------------
# 141_linkedlistcycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_hash=[]
        cur=head
        while cur:
            node_hash.append(cur)
            cur=cur.next
            if cur in node_hash:
                return True
        return False

## TORTISE HARE METHOD --
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False#-----------------------------------------------



#-----------------------------------------------
# 144_preorder

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[root.val]
        result+=self.preorderTraversal(root.left)
        result+=self.preorderTraversal(root.right)
        return result
        
#-----------------------------------------------



#-----------------------------------------------
# 145_postorder

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=self.postorderTraversal(root.left)
        result+=self.postorderTraversal(root.right)
        result.append(root.val)
        return result#-----------------------------------------------



#-----------------------------------------------
# 160_intersection

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b=headA,headB
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a


        # stack_a=[]
        # stack_b=[]
        # a,b=headA,headB
        # while a or b:
        #     if a in stack_b:
        #         return (f"intersected at {a.val}")
        #     else:
        #         stack_a.append(a)
        #     if b in stack_a:
        #         return (f"intersected at {b.val}")
        #     else:
        #         stack_b.append(b)
        # return "No intersection"
            
                #-----------------------------------------------



#-----------------------------------------------
# 168.excelcolumn
def convert(n):
    lst=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    res=''
    while n>0:
        res+=lst[(n-1)%26]
        n=(n-1)//26
    return res[::-1]
print(convert(int(input())))


   
    #-----------------------------------------------



#-----------------------------------------------
# 169_majorityelement
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,res=0,0
        for i in nums:
            if count==0:
                res=i
            count+=(1 if i==res else -1)
        return res



# def maj(nums):
#     l=len(nums)
#     stack={}
#     if l==1: return nums[0]
#     for i in nums:
#         if i in stack.keys():
#             stack[i]+=1
#             if stack[i]>len(nums)/2:
#                 return i
#         else:
#             stack[i]=1
import ast            
print(maj(ast.literal_eval(input())))#-----------------------------------------------



#-----------------------------------------------
# 171_excelcol
def title(cl):
    lst=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    res=0
    for i,n in enumerate(cl[::-1]):
        res+=(lst.index(n)+1)*26**(i)
    return res
print(title(input()))#-----------------------------------------------



#-----------------------------------------------
# 181rotate_arry
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def flip(nums,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            return
        flip(nums,0,len(nums)-1)
        flip(nums,0,k-1)
        flip(nums,k,len(nums)-1)
#-----------------------------------------------



#-----------------------------------------------
# 19remove_nth_lastnode
from typing import Optional
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        holder=ListNode(0,next=head)
        left=holder
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return holder.next#-----------------------------------------------



#-----------------------------------------------
# 202happynumber
class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1:
            if n in hset:
                return False
            else:
                hset.add(n)
                n = sum(int(i) ** 2 for i in str(n))
        return True
#-----------------------------------------------



#-----------------------------------------------
# 203linked_list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        dum_head = ListNode(-1)
        dum_head.next = head
        cur_node = dum_head
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dum_head.next
#-----------------------------------------------



#-----------------------------------------------
# 205Isomorphic
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_dict_a = {}
        hash_dict_b = {}
        for i, j in zip(s, t):
            if i not in hash_dict_a:
                hash_dict_a[i] = j
            elif hash_dict_a[i] != j:
                return False
            if j not in hash_dict_b:
                hash_dict_b[j] = i
            elif hash_dict_b[j] != i:
                return False

        return True


# ANOTHER SOLUTION -- 


def isIsomorphic(self, s: str, t: str) -> bool:
    zipped_set = set(zip(s, t))
    return len(zipped_set) == len(set(s)) == len(set(t))


print(Solution().isIsomorphic("badc", "baba"))
#-----------------------------------------------



#-----------------------------------------------
# 206.reverese_linkedlist
def reverseList(head):
    if not head:
        return None
    newhead=head
    if head:
        newHead=reverseList(head)
        head.next.next=head
    head.next=None
    return newhead
    #-----------------------------------------------



#-----------------------------------------------
# 219sliding_window
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
#-----------------------------------------------



#-----------------------------------------------
# 226.inverted_binarytree
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
#-----------------------------------------------



#-----------------------------------------------
# 228summary_ranges
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result_list = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    result_list.append(str(start))
                else:
                    result_list.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            result_list.append(str(start))
        else:
            result_list.append(f"{start}->{nums[-1]}")
        return result_list
print(Solution().summaryRanges([0,1,2,4,5,7]))

#-----------------------------------------------



#-----------------------------------------------
# 242valid_anagram
#-----------------------------------------------



#-----------------------------------------------
# 283move_zeros
import ast 
in_lst=ast.literal_eval(input())
def move_zeroes(in_lst):
    # for i in in_lst:
    #     if i==0:
    #         in_lst.remove(0)
    #         in_lst.append(0)
    # return in_lst
    l=0
    for r in range(len(in_lst)):
        if in_lst[r]:
            in_lst[l],in_lst[r]=in_lst[r],in_lst[l]
            l+=1
print(move_zeroes(in_lst))
#-----------------------------------------------



#-----------------------------------------------
# 290wrd_pattern
pattern=input()
s=input()
def word_pattern(pattern,s):
    s_lst=s.split(' ')
    stack_p={}
    stack_s={}
    if len(s_lst)!=len(pattern):
        return False
    for i,p in zip(s_lst,pattern):
        if p in stack_p and stack_p[p]!=i:
            return False
        if i in stack_s and stack_s[i]!=p:
            return False
        stack_p[p]=i
        stack_s[i]=p
    return True
print(word_pattern(pattern,s))
#-----------------------------------------------



#-----------------------------------------------
# 2SUM
def twoSum(nums,target):
    temp=nums.copy()
    temp.sort()
    x=0
    y=len(nums)-1
    while x < len(nums):
        while y >0:
            i=temp[x]
            m=temp[y]
            if target<i+m:
                y-=1
            elif target>i+m:
                x+=1
            else:
                return [nums.index(i),nums.index(m)]
print('ENTER list')
nums=list(map(int,input().split(",")))
print('Enter target')
target=int(input())
print(twoSum(nums,target))  #-----------------------------------------------



#-----------------------------------------------
# 2_addtwonums
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s_1,s_2=self.get_str(l1),self.get_str(l2)
        res=str(int(s_1)+int(s_2))[::-1]
        return build_listnode([i for i in res])
    def get_str(self,l):
        if not l:
            return ""
        return self.get_str(l.next)+str(l.val)
import ast
l1=ast.literal_eval(input())
l2=ast.literal_eval(input())
def build_listnode(l1):
    root=ListNode(l1[0])
    cur=root
    for i in l1[1:]:
        node=ListNode(i)
        cur.next=node
        cur=node
    return root
r1=build_listnode(l1)
r2=build_listnode(l2)

Solution().addTwoNumbers(r1,r2)#-----------------------------------------------



#-----------------------------------------------
# 300_longest_asc_seq
import ast

input = ast.literal_eval(input())


def lenghtoflis(nums):
    hash_list = [1] * len(nums)
    for i in range(len(nums), -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                hash_list[i] = max(hash_list[i], hash_list[j] + 1)
    return max(hash_list)


print(lenghtoflis(input))
#-----------------------------------------------



#-----------------------------------------------
# 30substring_allwords
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_span=len(words[0])
        len_substr=word_span*len(words)
        words_map={i:words.count(i) for i in set(words)}
        if len_substr>len(s):
            return []
        i,res=0,[]
        while i<(len(s)-len_substr)+1:
            cur_str=s[i:i+len_substr]
            p,str_lst=0,[]
            while p<len(cur_str):
                str_lst.append(cur_str[p:p+word_span])
                p+=word_span
            # for word in words: 
            #     if word in str_lst:
            #         str_lst.remove(word)
            #     else:
            #         break
            sub_map={i:str_lst.count(i) for i in set(str_lst)}
            if sub_map==words_map:
                res.append(i)
            i+=1
        return res

print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))#-----------------------------------------------



#-----------------------------------------------
# 322coinchange
import ast
input=ast.literal_eval(input())
def coinchange(coins,amount):
    dp=[amount+1]*(amount+1)
    dp[0]=0
    for amt in range(1,amount+1):
        for coin in coins:
            if amt-coin>=0:
                dp[amt]=min(dp[amt],1+dp[amt-coin])
    return dp[amount] if dp[amount]!=amount+1 else -1
print(coinchange(input,6249))#-----------------------------------------------



#-----------------------------------------------
# 32_longest_paranthesis
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
Solution().longestValidParentheses(")))()(()")#-----------------------------------------------



#-----------------------------------------------
# 377combination_sum
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[total]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0
            count = 0
            for num in nums:
                if n - num < 0:
                    break
                count += helper(n - num)
            memo[n] = count
            return count

        return helper(target)
#-----------------------------------------------



#-----------------------------------------------
# 39_combinationsum
def combinationsum(lst, target):
    result = []

    def dfs(i, cur, sum):
        if sum == target:
            result.append(cur.copy())
            return
        if sum > target or i >= len(lst):
            return
        cur.append(lst[i])
        dfs(i, cur, sum + lst[i])
        cur.pop()
        dfs(i + 1, cur, sum)

    dfs(0, [], 0)
    return result


print(combinationsum([2, 3, 6, 7], 7))
#-----------------------------------------------



#-----------------------------------------------
# 3SUM
#     # if nums.count(0)==len(nums) and len(nums)>2:
#     #     return [[0,0,0]]
#     nums.sort()
#     span = len(nums)
#     k = 0
#     j, l = k + 1, span - 1
#     lst = []
#     while k < span - 2:
#         if j < l:
#             sum = nums[k] + nums[j] + nums[l]
#             if sum < 0:
#                 while nums[j] == nums[j + 1] and j < l - 1:
#                     j += 1
#                 j += 1
#             elif sum > 0:
#                 while nums[l] == nums[l - 1] and j < l - 1:
#                     l -= 1
#                 l -= 1
#             elif sum == 0:
#                 lst.append([nums[k], nums[j], nums[l]])
#                 print([nums[k], nums[j], nums[l]], " K= ", k)
#                 while nums[j] == nums[j + 1] and j < l - 1:
#                     j += 1
#                 j += 1
#         else:
#             while nums[k] == nums[k + 1] and k < span - 2:
#                 k += 1
#             k += 1
#             j, l = k + 1, span - 1
#     return lst


def threeSum(nums):
    if len(nums) == 3 and sum(nums) == 0:
        return [nums]
    nums.sort()
    i, j, k = 0, 1, len(nums) - 1
    result = []
    while i < len(nums) - 3:
        target_sum = -nums[i]
        while j < k:
            if nums[j] + nums[k] > target_sum:
                k -= 1
            elif nums[j] + nums[k] < target_sum:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
        i += 1
        while nums[i] == nums[i - 1] and i < len(nums) - 2:
            i += 1
        j = i + 1
        k = len(nums) - 1
    return result


print(threeSum(list(map(int, input().split(",")))))
#-----------------------------------------------



#-----------------------------------------------
# 3SUMCLOSEST
def threeSumclosest(nums,target):
    nums.sort()
    span=len(nums)
    diff=abs(target-(nums[0]+nums[1]+nums[span-1]))
    result=nums[0]+nums[1]+nums[span-1]
    for i in range(0,span-2):
        j,k=i+1,span-1
        while nums[j]==nums[j+1] and j+1<k:
            j+=1
        if nums[j-1]==nums[j] and (j-1)!=i:
            j-=1
        while nums[k]==nums[k-1] and j+1<k:
            k-=1
        while (j<k):
            temp=(nums[i]+nums[j]+nums[k])
            if temp>target:
                k-=1
            elif temp<target:
                j+=1
            else:
                return temp
            if diff>abs(target-temp):
                diff=abs(target-result)
                result=temp
            if diff==0:
                return result
    return result
nums=list(map(int,input().split(",")))
target=int(input())
print(threeSumclosest(nums,target))#-----------------------------------------------



#-----------------------------------------------
# 3_longest_substr
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set=[]
        max_substr=0
        for i in s:
            if i not in temp_set:
                temp_set.append(i)
                max_substr=max(max_substr,len(temp_set))
            else:
                temp_set=temp_set[temp_set.index(i)+1:]
                temp_set.append(i)
        return max_substr
    
print(Solution().lengthOfLongestSubstring('aabaab!bb'))#-----------------------------------------------



#-----------------------------------------------
# 3_longsubstring
""" 
This is a classic sliding window problem. 
When we need to find "longest" something, try to use sliding window. 
you start with no set and then keep updating the set as you traverse a given string/list
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp, result = 0, 0
        char_set = set()
        for rp in range(len(s)):
            while s[rp] in char_set:
                char_set.remove(s[lp])
                lp += 1
            char_set.add(s[rp])
            result = max(result, rp - lp + 1)
        return result
#-----------------------------------------------



#-----------------------------------------------
# 40_combinationsum2
def combinationsum2(lst, target):
    result = []
    lst.sort()

    def dfs(i, cur, sum):
        if sum == target:
            result.append(cur)
            return
        if sum > target:
            return
        for i in range(i, len(lst)):
            dfs(i, cur.append(lst[i]), sum + lst[i])

    dfs(0, [], 0)
    return result


print(combinationsum2([10, 1, 2, 7, 6, 1, 5], 8))
#-----------------------------------------------



#-----------------------------------------------
# 416partitionequalsubset
def canPartition(nums):
    if sum(nums) % 2!=0:
        return False
    target=sum(nums)//2
    dp=set()
    dp.add(0)
    for i in range(len(nums)-1):
        nextdp=set()
        for t in dp:
            if t+nums[i]==target:
                return True
            nextdp.add(t)
            nextdp.add(t+nums[i])
        dp=nextdp
    return True if target in dp else False
print(canPartition([1,5,11,5]))#-----------------------------------------------



#-----------------------------------------------
# 42trap_rainwater
class Solution:
    def trap(self, ht: List[int]) -> int:
        l, r = 0, len(ht) - 1
        l_max, r_max, res = ht[l], ht[r], 0
        while l < r:
            if ht[l] < ht[r]:
                l += 1
                l_max = max(ht[l], l_max)
                res += l_max - ht[l]
            else:
                r -= 1
                r_max = max(ht[r], r_max)
                res += r_max - ht[r]
        return res
#-----------------------------------------------



#-----------------------------------------------
# 435.non-overlaps
def overlaps(intervals):
    count = 0
    intervals.sort()
    previous_end = intervals[0][0]
    for i, j in intervals[1:]:
        if previous_end <= i:
            previous_end = j
        else:
            previous_end = min(j, previous_end)
            count += 1
    return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(overlaps(intervals))
#-----------------------------------------------



#-----------------------------------------------
# 441arrange_coins
def arrange_coins(n):
    rows = 0
    steps = 0
    while steps < n:
        rows += 1
        steps += rows
    return rows if steps == n else rows - 1


print(arrange_coins(5))


def binary_coin_search(n):
    l, r = 1, n
    res = 0
    while l <= r:
        mid = (l + r) // 2
        coins = (mid / 2) * (mid + 1)
        if coins > n:
            r = mid - 1
        else:
            l = mid + 1
            res = max(mid, res)
    return res
#-----------------------------------------------



#-----------------------------------------------
# 448missingnums
def disappeared(nums):
    hsh = []
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])
    for r, i in enumerate(nums):
        if r > 0:
            hsh.append(i + 1)
    return hsh


print(disappeared([4, 3, 2, 7, 8, 2, 3, 1]))
#-----------------------------------------------



#-----------------------------------------------
# 455assign_cookies
def cookies(childs, cookies):
    childs.sort()
    cookies.sort()
    count = 0
    childs_ptr = len(childs) - 1
    cookies_ptr = len(cookies) - 1
    while childs_ptr >= 0 and cookies_ptr >= 0:
        if cookies[cookies_ptr] >= childs[childs_ptr]:
            count += 1
            cookies_ptr -= 1
            childs_ptr -= 1
        else:
            childs_ptr -= 1
    return count


print(cookies([10, 9, 8, 7], [5, 6, 7, 8]))
#-----------------------------------------------



#-----------------------------------------------
# 459Repeatedsubstring
def repeatedsubstr(s):
    N = len(s)

    def pattern(n):
        for i in range(0, N - n, n):
            if s[i : i + n] != s[i + n : i + n * 2]:
                return False
        return True

    for i in range(1, len(s) // 2 + 1):
        if pattern(i):
            return True
    return False


print(repeatedsubstr("abababab"))


#  Solution 2:
def repeatedsubstr(s):
    ds = (s * 2)[1:-1]
    return s in ds
#-----------------------------------------------



#-----------------------------------------------
# 463.island_perimiter
def island(grid):
    visit=set()
    
    def dfs(i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) \
            or grid[i][j] == 0:
                return 1
        if (i,j) in visit:
            return 0
        visit.add((i,j))
        peri=dfs(i-1,j)
        peri+=dfs(i+1,j)
        peri+=dfs(i,j-1)
        peri+=dfs(i,j+1)
        return peri
    
    
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:return dfs(i,j)

grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(island(grid))#-----------------------------------------------



#-----------------------------------------------
# 46permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, callstack=[]):
            callstack.append(path)
            print(callstack)
            if not nums:
                result.append(path)
                callstack.pop()
                print(f"result={result}")
 
                print(callstack)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1 :], path + [nums[i]], callstack)

        result = []
        backtrack(nums, [])
        return result


print(Solution().permute([1, 2, 3]))
#-----------------------------------------------



#-----------------------------------------------
# 47_permutations_2
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash_map={n:nums.count(n) for n in nums}
        def df():
            if len(temp)==len(nums):
                result.append(temp.copy())
                return
            for n in hash_map:
                if hash_map[n]>0:
                    temp.append(n)
                    hash_map[n]-=1
                    df()
                    hash_map[n]+=1
                    temp.pop()
        result,temp=[],[]
        df()
        return result
print(Solution().permuteUnique([1,1,3]))#-----------------------------------------------



#-----------------------------------------------
# 482Licensekey
def lk(s, k):
    s = s.replace("-", "").upper()[::-1]
    st = ""
    for i in range(0, len(s), k):
        st += s[i : i + k] + "-"
    st = st[::-1]
    st = st.replace("-", "", 1)
    return st


s = "2-5g-3-J"
k = 2
print(lk(s, k))
#-----------------------------------------------



#-----------------------------------------------
# 4SUM
def foursum(nums, target):
    ct = 1
    i = 0
    while True:
        if nums[i] == nums[i + 1]:
            ct += 1
            if ct > 4:
                nums.pop(i + 1)
            else:
                i += 1
        else:
            ct = 1
            i += 1
        if i == (len(nums) - 1):
            break
    result = []
    HT = {}
    unq = list(set(nums))
    for i in list(set(nums)):
        HT[i] = nums.count(i)
    HT = dict(sorted(HT.items(), key=lambda x: x[1], reverse=True))
    for i in dict(list(HT.items())[:-3]):
        if HT[i] == 4:
            if i * 4 == target:
                result.append([i, i, i, i])
            if (len(HT) - list(HT.keys()).index(i)) > 3:
                ind = list(HT.keys()).index(i)
                for j in dict(list(HT.items())[ind:]):
                    if HT[j] > 2:
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                        if (i + 3 * j) == target:
                            result.append([i, j, j, j])
                    if HT[j] == 2:
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
                    if HT[j] == 1:
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
            if (len(HT) - list(HT.keys()).index(i)) > 3:
                ind = list(HT.keys()).index(i)
                for j in dict(list(HT.items())[ind:]):
                    if HT[j] >= 2:
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                    else:
                        inj = list(HT.keys()).index(j)
                        for k in dict(list(HT.items())[inj:]):
                            if (i * 2 + j + k) == result:
                                result.append([i, i, j, k])

            if HT[i] == 1:
                return result


nums = list(map(int, input().split(",")))
target = int(input())
print(foursum(nums, target))


#  if HT[i]>=3:
#                 ind=list(HT.keys()).index(i)
#                 for j in dict(list(HT.items())[ind:]):
#                     if (i*3+j)==target:
#                         result.append([i,i,i,j])
#             if HT[i]>=2:
#                 ind=list(HT.keys()).index(i)
#                 for j in dict(list(HT.items())[ind:]):
#                     if HT[j]>=2:
#                         if (i+j)*2==result:
#                             result.append([i,i,j,j])
#                     else:
#                         inj=list(HT.keys()).index(j)
#                         for k in dict(list(HT.items())[inj:]):
#                             if (i*2+j+k)==result:
#                                 result.append([i,i,j,k])
#-----------------------------------------------



#-----------------------------------------------
# 51_N_queens
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]
        col_set,diag_up,diag_down=set(),set(),set()
        def bt(row):
            if row==n:
                cpy=["".join(rw) for rw in board]
                print(cpy)
                res.append(cpy)
                return 
            print(board)
            for col in range(n):
                if col in col_set or row+col in diag_up or row-col in diag_down:
                    continue
                col_set.add(col)
                diag_up.add(row+col)
                diag_down.add(row-col)
                board[row][col]='Q'

                bt(row+1)
                
                col_set.remove(col)
                diag_up.remove(row+col)
                diag_down.remove(row-col)
                board[row][col]='.'
        bt(0)
        return res
print(Solution().solveNQueens(4))#-----------------------------------------------



#-----------------------------------------------
# 52.N-queen2
class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        diag_up, diag_dn = set(), set()
        res = 0

        def bt(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if col in col_set or (row - col) in diag_up or (row + col) in diag_dn:
                    continue
                col_set.add(col)
                diag_up.add(row - col)
                diag_dn.add(row + col)
                bt(row + 1)
                col_set.remove(col)
                diag_up.remove(row - col)
                diag_dn.remove(row + col)

        bt(0)
        return res


print(Solution().totalNQueens(4))
#-----------------------------------------------



#-----------------------------------------------
# 53max_subarray
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        cur_sum=0
        for i in nums:
            if cur_sum<0:
                cur_sum = 0
            cur_sum +=i
            max_sum=max(max_sum,cur_sum)
        return max_sum
print(Solution().maxSubArray([5,4,-1,7,8]))#-----------------------------------------------



#-----------------------------------------------
# 56.merge_intervals
def merge(intervals):
    intervals.sort()
    result=[intervals[0]]
    for indx in range(1,len(intervals)):
        if result[-1][1]>=intervals[indx][0]:
            temp=result[-1]+intervals[indx]
            result[-1]=[min(temp),max(temp)]
        else:
            result.append(intervals[indx])
    return result
intervals=[[1,4],[0,0]]
print(merge(intervals))#-----------------------------------------------



#-----------------------------------------------
# 57.insert_interval
def merge(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort()
    result=[intervals[0]]
    for indx in range(1,len(intervals)):
        if result[-1][1]>=intervals[indx][0]:
            temp=result[-1]+intervals[indx]
            result[-1]=[min(temp),max(temp)]
        else:
            result.append(intervals[indx])
    return result
intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval=[4,8]
print(merge(intervals,newInterval))#-----------------------------------------------



#-----------------------------------------------
# 5_longpal

def longpal(s):
    N=len(s)
    def lp(l,r):
        while l>=0 and r<N:
            if s[l]!=s[r]: break
            l-=1
            r+=1
        return l+1,r
    start,end=0,0
    for i in range(N):
        l,r=lp(i,i)
        if r-l>end-start:
            start=l
            end=r
        l,r=lp(i,i+1)
        if r-l>end-start:
            start=l
            end=r
    return s[start:end]






    # for i in range(0,len(s)):
    #     for j in range(1,len(s)+1):
    #         if s[i:j]==s[i:j][::-1] and long_pal<(j-i):
    #             long_pal=(j-i)
    #             res=s[i:j]
    # return res

print(longpal(input()))#-----------------------------------------------



#-----------------------------------------------
# 617.merge_binaries
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergetrees(r1, r2):
    if r1 is None and r2 is None:
        return None
    val1 = r1.val if r1 else 0
    val2 = r2.val if r2 else 0
    r3 = TreeNode(val1 + val2)
    r3.left = mergetrees(r1.left if r1 else None, r2.left if r2 else None)
    r3.right = mergetrees(r1.right if r1 else None, r2.right if r2 else None)
    return r3


#-----------------------------------------------



#-----------------------------------------------
# 62uniquepaths
import functools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(None)
        def defs(i,j):
            if i>=m or j>=n: return 0
            if i==m-1 and j == n-1: return 1
            return defs(i+1,j)+defs(i,j+1)
        return defs(0,0)
print(Solution().uniquePaths(3,7))#-----------------------------------------------



#-----------------------------------------------
# 6_zigzag
def convert(s: str, n: int) -> str:
    if n==1: return s
    dct={r:"" for r in range(1,n+1)}
    r,up=1,True
    for i in s:
        dct[r]+=i
        if (r==1) or ((r<n) and up):
            r+=1
            up=True
        else:
            r-=1
            up=False
    return ''.join([dct[i] for i in dct.keys()])
print(convert(input(),int(input())))#-----------------------------------------------



#-----------------------------------------------
# 74search2dmatrix
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            if target>=matrix[i][0] and target<=matrix[i][n-1]:
                l,r,mid=0,n-1,n+1
                while l<=r and mid!=1:
                    mid=l+int((r-l)/2)  
                    if target==matrix[i][mid]:
                        return True
                    elif target<matrix[i][mid]:
                        r=mid-1
                    else:
                        l=mid-1
                return False
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))#-----------------------------------------------



#-----------------------------------------------
# 75_sortcolors
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map={i:nums.count(i) for i in range(3)}
        j=0
        for i in range(len(nums)):
            while hash_map[j]==0:
                j+=1
            nums[i]=j
            hash_map[j]-=1

                
        return nums
print(Solution().sortColors(nums=[2,0,2,1,1,0]))#-----------------------------------------------



#-----------------------------------------------
# 76_min_window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='': return ''
        l,r=0,1
        lst=[i for i in t]
        t_map={i:lst.count(i) for i in set(lst)} 
        t_span=len(t_map)
        h_map={i:0 for i in t_map}
        check_span=0
        while r<len(s):
            if s[l] in h_map:
                h_map[s[l]]+=1
                if h_map[s[l]]>=t_map[s[l]]:
                    check_span+=1
            if check_span>=t_span:
                result=s[l:r+1]
            if r<len(s): r+=1
            else: l-=1
        return result
            
print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))#-----------------------------------------------



#-----------------------------------------------
# 77combinations
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
print(Solution().combine(n=4,k=2))#-----------------------------------------------



#-----------------------------------------------
# 78subsets
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(i=0,path=[]):
            if i>=len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            bt(i+1,path)
            path.pop()
            bt(i+1,path)
        bt()
        return res
    
print(Solution().subsets(nums=[1,2,3]))#-----------------------------------------------



#-----------------------------------------------
# 80sortyarray_2

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,0
        while r<len(nums):
            count=1
            while r<len(nums)-1 and nums[r]==nums[r+1]:
                r+=1
                count+=1
            for i in range(min(2,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
print(Solution().removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))
#-----------------------------------------------



#-----------------------------------------------
# 82removeduplicates
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        l=dummy
        r=l.next
        while r:
            if r and r.next and r.val==r.next.val:
                while r.next and r.val==r.next.val:
                    r=r.next
                l.next=r.next
            else: l=l.next
            r=r.next
        return dummy.next
ar=[1,2,3,3,4,4,5]
cur_node=ListNode(ar[0])
head=cur_node
for i,val in enumerate(ar[1:]):
    node=ListNode(val)
    cur_node.next=node
    cur_node=node
x=Solution().deleteDuplicates(head)
while x:
    print(x.val)
    x=x.next
...
#-----------------------------------------------



#-----------------------------------------------
# 86partitionlist
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        cur_node=dummy.next
        less_head=None
        more_head=None
        while cur_node.next:
            if cur_node.val<x:
                if not less_head:
                    less_head=ListNode(val=cur_node.val)
                    les_cur=less_head
                    continue
                les_cur.next=ListNode(val=cur_node.val)
                les_cur=les_cur.next
            else:
                if not more_head:
                    more_head=ListNode(val=cur_node.val)
                    more_cur=more_head
                    continue
                more_cur.next=ListNode(val=cur_node.val)
                more_cur=more_cur.next
            cur_node=cur_node.next
        les_cur.next=more_head
        return less_head

lst = [1,4,3,2,5,2]
x = 3
head=ListNode(val=lst[0])
cur_node=head
for i in lst[1:]:
    cur_node.next=ListNode(i)
    cur_node=cur_node.next
Solution().partition(head,x)#-----------------------------------------------



#-----------------------------------------------
# 97interleavingstrings
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        span1,span2,span3=len(s1),len(s2),len(s3)
        if (span1+span2)!=span3: return False
        p1,p2,p3=0,0,0
        while p1<span1 and p2<span2 and p3<span3:
            if s1[p1]==s3[p3]:
                p1+=1
                p3+=1
            elif s2[p2]==s3[p3]:
                p2+=1
                p3+=1
            else:
                return False
        return s3[p3:]==s1[p1:]+s2[p2:]
print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))#-----------------------------------------------



#-----------------------------------------------
# addbinary
def mySqrt(x: int) -> int:
    if x==0 or x==1:
        return 0
    L,R=1,x//2
    while L<=R:
        mid=(L+R)//2
        if mid==x//mid:
            return mid
        elif mid<x//mid:
            L=mid+1
        else:
            R=mid-1
    return R
    
x=int(input())
print(mySqrt(x))#-----------------------------------------------



#-----------------------------------------------
# api_calls_decorator
from time import time
def rate_limit(period,max_call_count):
    def decorator(func):
        call_count=0
        last_call=time()
        def wrapper(*args, **kwargs):
            nonlocal call_count,last_call
            elapsed_time=time()-last_call
            if elapsed_time>period:
                call_count=0
                last_call=time.time()
            if call_count>=max_call_count:
                raise Exception("Rate Limit Exceeded. Please try again later")
            call_count+=1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(period=10,max_call_count=6)
def api_call():
    print('API EXCEUTED SUCCESSFULLY')


for i in range(10):
    try:
        api_call()
    except Exception as e:
        print(f"EXCEPTION OCCURED: {e}")#-----------------------------------------------



#-----------------------------------------------
# calculate
import pandas
import numpy as np
array=input()#-----------------------------------------------



#-----------------------------------------------
# classes
class Robot:
    def __init__(self,name: str,color: str,weight:int):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print(f"my namee is {self.name}")
r1=Robot('Tom','red',30)
r2=Robot('Jerry','blue',40)
r1.introduce()
r2.introduce()

# ADDING RELATIONSHIPS TO VARIOUS OBJECTS AND SETTING STATES

class Person:
    def __init__(self,name:str,personality:str,isSitting:bool,robotowned:Robot):
        self.name=name
        self.personality=personality
        self.isSitting=isSitting
        self.robotowned=robotowned
    def sit_down(self):
        self.isSitting=True
        print(f"{self.name} is_sitting {self.isSitting}")
    def stand_up(self):
        self.isSitting=False
        print(f"{self.name} is_sitting {self.isSitting}")
p1=Person('Alice','aggressive',False,r1)
p2=Person('Becky','talkative',True,r2)
p1.sit_down()
p2.sit_down()
p2.stand_up()#-----------------------------------------------



#-----------------------------------------------
# classes_polymorphism
from abc import ABCMeta, abstractmethod

x = [1, 2, 3]
for i in x[:]:
    x.append(i + 1)
    print(x)


class Jungle(metaclass=ABCMeta):
    def __init__(
        self,
        name="Unknown",
    ):
        self.name = name

    def introduce(self):  # no need to add name here again.
        print(f"Welcome to the {self.name} Jungle")

    @abstractmethod
    def scarysound(self):
        ...


class Bungle:
    def __init__(
        self,
        name="Unknown",
    ):
        self.name = name

    def introduce(self):
        print(f"welcome to the {self.name} Bungle")


""" 
This is polymorphism because the method "introduce" is local to two different
classes but python allows for same method to be used in different classes. 
"""

amazon = Jungle("Amazon")
bamazon = Bungle("Bamazon")
amazon.introduce()
bamazon.introduce()


class RateJungle(Jungle):
    def __init__(self, name, rating=None):
        super(RateJungle, self).__init__(name)  # inheriting the constructor of class
        self.rating = rating

    def printRating(self):
        print(f"The Jungle rating is {self.rating} with {self.name}")


r = RateJungle("Meher", 3)
r.printRating()
r.introduce()


class Insect(Jungle):
    def scarysound(self):
        print("insects don't care about scary sounds")


i = Insect()
i.scarysound()
#-----------------------------------------------



#-----------------------------------------------
# climbingstairs
val=int(input())
def stairs(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
print(stairs(val))

# n+(n//2)+(1+(n-1)//2)#-----------------------------------------------



#-----------------------------------------------
# coderbyte1
def TwoSum(arr):
    recieved_arr=arr.copy()
    target=arr[0]
    arr.pop(0)
    arr.sort()
    x,y=0,len(arr)-1
    lst=[]
    while x<len(arr) and y>x:
        i,m=arr[x],arr[y]
        if target<i+m:
            y-=1
            continue
        elif target>i+m:
            x+=1
            continue
        else:
            if recieved_arr.index(i)<=recieved_arr.index(m):
                lst.append([i,m])
                x+=1
            else:
                lst.append([m,i])
                x+=1
    
    if str=="":
        return -1
    else:
        return str.strip()


print(TwoSum([17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]))



def split_array_evenly(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return None

    target_sum = total_sum // 2
    subset = []
    result = []

    def find_subsets_with_sum(index, current_sum):
        if current_sum == target_sum:
            result.append(subset[:])
        elif current_sum < target_sum and index < len(nums):
            num = nums[index]
            subset.append(num)
            find_subsets_with_sum(index + 1, current_sum + num)
            subset.pop()
            find_subsets_with_sum(index + 1, current_sum)

    find_subsets_with_sum(0, 0)
    return result

# Example usage
nums = [1, 5, 11, 5]
split_sets = split_array_evenly(nums)
if split_sets:
    print("Possible split:")
    print("Set 1:", split_sets[0])
    print("Set 2:", split_sets[1])
else:
    print("No even split possible.")#-----------------------------------------------



#-----------------------------------------------
# combinelists
import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
L1=ast.literal_eval(input())
L2=ast.literal_eval(input())
def build_nodelist(L1):
    if len(L1) ==0:
        return None
    LN=ListNode(val=L1[0])
    CURNODE=LN
    for i in L1[1:]:
        NEW_NODE=ListNode(val=i)
        CURNODE.next=NEW_NODE
        CURNODE=NEW_NODE
    return LN
LN1=build_nodelist(L1)
LN2=build_nodelist(L2)
def combine_nodes(LN1,LN2):
    C1,C2=LN1,LN2
    if LN1 is None:
        return LN2
    elif LN2 is None:
        return LN1
    if C1.val<C2.val:
        RES=ListNode(val=C1.val)
        CURNODE=RES
        C1=C1.next
    elif C1.val==C2.val:
        RES=ListNode(val=C1.val)
        C1=C1.next
        CURNODE=RES
        CURNODE.next=ListNode(val=C2.val)
        CURNODE=CURNODE.next
        C2=C2.next
    else:
        RES=ListNode(val=C2.val)
        CURNODE=RES
        C2=C2.next
    while C1 and C2 is not None:
        if C1.val<C2.val:
            CURNODE.next=ListNode(val=C1.val)
            CURNODE=CURNODE.next
            C1=C1.next
        elif C1.val==C2.val:
            CURNODE.next=ListNode(val=C1.val)
            C1=C1.next
            CURNODE=CURNODE.next
            CURNODE.next=ListNode(val=C2.val)
            CURNODE=CURNODE.next
            C2=C2.next
        else:
            CURNODE.next=ListNode(val=C2.val)
            CURNODE=CURNODE.next
            C2=C2.next
    CURNODE.next=C1 or C2
    return RES
RES=combine_nodes(LN1,LN2)
RESULT=[]
CUR=RES
while CUR is not None:
    RESULT.append(CUR.val)
    CUR=CUR.next
print(RESULT)

#-----------------------------------------------



#-----------------------------------------------
# contains_duplicates
class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False


import ast

print(Solution().containsDuplicate(ast.literal_eval(input())))
#-----------------------------------------------



#-----------------------------------------------
# decorators
def multiply_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"function: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} with result: {result}")
        return result
    return wrapper


@multiply_decorator
def multiply(x,y,z=None,k=None):
    return x*y
x,y=5,5
result = multiply(x,y,z=5,k=10)
print(f"return: {result}")#-----------------------------------------------



#-----------------------------------------------
# decorator_class
def class_type(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        print(result)
        print(f"class: {type(result)}")
        return result
    return wrapper
@class_type
def string_concat(x,y):
    return x+" "+ y
x,y='abc','xyz'
string_concat(x,y)#-----------------------------------------------



#-----------------------------------------------
# deleteduplicatenodes
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
print(result_list)#-----------------------------------------------



#-----------------------------------------------
# deq
from collections import deque

people= ['Mario', 'Luigi', 'Toad']
queue= deque(people)

queue.append('Browser')
print(queue[1])

queue.popleft()
print(queue)
queue.appendleft('Daisy')
print(queue)
queue.rotate(-1)
print(queue)
queue.extend(['Shyg','Yoshi'])
print(queue)
queue.reverse()
print(queue)#-----------------------------------------------



#-----------------------------------------------
# emr_spark_job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd

S3_DATA_SOURCE_PATH = "s3://myawsbucket-ajarabani/PKL/RAW_LBR.PKL"
S3_DATA_OUTPUT_PATH = "s3://myawsbucket-ajarabani/data-output"
raw_lbr = pd.read_pickle(S3_DATA_SOURCE_PATH)


def main():
    spark = SparkSession.builder.appName("demoapp").getOrCreate()
    raw_lbr = spark.createDataFrame(raw_lbr)
    print(f"Total number of records {raw_lbr.count()}")
    raw_lbr = raw_lbr.withColumn("HRS/EA", col("HRS_WORKED") / col("OP_QTY"))
    raw_lbr.select("OP_QTY").show()
    raw_lbr.write.mode("overwrite").parquet(S3_DATA_OUTPUT_PATH)
    print(f"Selected data was successfully saved to s3 {S3_DATA_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
#-----------------------------------------------



#-----------------------------------------------
# firststringocurance
needle=input()
haystack=input()
def needle_index(haystack,needle):
    result=0
    while haystack!="":
        if haystack.startswith(needle):
            return result
        else:
            haystack=haystack[1:]
            result+=1
    return -1
result=needle_index(haystack,needle)
print(result)
    
#-----------------------------------------------



#-----------------------------------------------
# folder_prints
file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/dack/diary/2023-04-03.txt",
    "/gome/back/biry/xly.txt"
]

file_paths = [
    "/a/b/e",
    "/a/b/h",
    "/a/b/i"
    "/a/c/f",
    "/a/d/g",
    "/a/d/g/l"
    ]
file_paths.sort
class node:
    def __init__(self, name=None):
        self.name: str = name
        self.files: list = []
        self.folders = {}

    def add_folder(self, path_list):
        cur_node = self
        for i in path_list:
            if i not in cur_node.folders:
                cur_node.folders[i] = node(i)
            cur_node = cur_node.folders[i]

    def add_files(self, path_list, file):
        cur_node = self
        for i in path_list:
            if i not in cur_node.folders:
                cur_node.folders[i] = node(i)
            cur_node = cur_node.folders[i]
        cur_node.files.append(file)

    def print_structure(self, cur_node=None, indent=0):
        if not cur_node:
            return
        for name, next_nodes in cur_node.folders.items():
            print("  " * (indent) + "-" + name)
            self.print_structure(next_nodes, indent + 1)
        for file in cur_node.files:
            print(" " * (indent + 1) + "-" + file)


structure = node()
for i in file_paths:
    nodes = i.split("/")[1:]
    files = nodes[-1]
    folders = nodes[:-1]
    structure.add_folder(folders)
    structure.add_files(folders, files)
structure.print_structure(structure)
#-----------------------------------------------



#-----------------------------------------------
# folder_struct
file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/dack/diary/2023-04-03.txt",
    "/gome/back/biry/xly.txt"
]

from typing import List
class Node:
    def __init__(self,name=None,folders={},files=[]):
        self.name:str=name
        self.folders:dict[str,Node]={}
        self.files:List[str] = []
    def add_folders(self,path_list:List[str]):
        cur_node=self
        for folder in path_list:
            if folder not in cur_node.folders:
                cur_node.folders[folder]=Node()
            cur_node=cur_node.folders[folder]
    def add_files(self,folder_list,file:str):
        cur_node=self
        for folder in folder_list:
            if folder not in cur_node.folders:
                cur_node.folders[folder]=Node()
            cur_node=cur_node.folders[folder]
        cur_node.files.append(file)
    def print_tree(self,cur_node,indent=0):
        if not cur_node:
            return
        for folder_name,folder in cur_node.folders.items():
            print(' '*indent+f'-{folder_name}')
            self.print_tree(folder,indent+1)
        for file in cur_node.files:
            print(' '*(indent+1)+f'-{file}')
tree=Node()
for i in file_paths:
    folders=i.split('/')[1:]
    file=folders.pop()
    tree.add_folders(folders)
    tree.add_files(folders,file)
tree.print_tree(tree)

    
    #-----------------------------------------------



#-----------------------------------------------
# gcd_string
from math import gcd


def gcd_strings(str1, str2):
    if str1 + str2 == str2 + str1:
        str = str1 + str2
        return str[: gcd(len(str1), len(str2))]
    return ""


str1 = "xyz"
str2 = "xyzxyz"
#-----------------------------------------------



#-----------------------------------------------
# gcenter_string
def str_output(in_str):
    lst=[i for i in in_str]
    uniques=list(set(lst))
    uniques.sort()
    result_list=[[i,lst.count(i)] for i in uniques] #[[a,3],[b,3],[c,2]]
    result=""
    for i in result_list:
        result+=str(i[0])+str(i[1])
    return result

in_str="aabbbacc"
print(str_output(in_str))

#-----------------------------------------------



#-----------------------------------------------
# hackerrank_atm
from typing import Optional,Tuple,Dict
Action = str

class State:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

def login_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param == atm_password:
        return True, atm_current_balance, None
    else:
        return False, atm_current_balance, None

def logout_checker(action_param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    return True, atm_current_balance, None

def deposit_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param is not None:
        amount = int(action_param)
        return True, atm_current_balance + amount, None
    return False, atm_current_balance, None

def withdraw_checker(action_param: str, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    if action_param is not None:
        amount = int(action_param)
        if atm_current_balance >= amount:
            return True, atm_current_balance - amount, None
    return False, atm_current_balance, None

def balance_checker(action_param: Optional[str], atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional[int]]:
    return True, atm_current_balance, atm_current_balance

# Implement the transition_table here
transition_table = {
    State("unauthorized"): [
        ("login", login_checker, State("authorized"))
    ],
    State("authorized"): [
        ("logout", logout_checker, State("unauthorized")),
        ("deposit", deposit_checker, State("authorized")),
        ("withdraw", withdraw_checker, State("authorized")),
        ("balance", balance_checker, State("authorized"))
    ]
}

# Look for the implementation of the ATM class in the below Tail section
class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: Action, param: Optional[str]) -> Tuple[bool, Optional[int]]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

if __name__ == "__main__":
    # Sample usage:
    input_password = 'hacker' # input()
    init_balance = 10 # int(input())

    # Set the initial state to "unauthorized"
    atm = ATM(State("unauthorized"), init_balance, input_password, transition_table)

    inp = ["login hacker","depoist 10"]  #int(input())
    q=len(inp)
    for i in inp:
        # action_input = input().strip().split()
        action_input=i.split(' ')
        action_name = action_input[0]
        action_param = action_input[1] if len(action_input) > 1 else None

        if action_name in ["deposit", "withdraw"]:
            action_param = int(action_param)

        success, res = atm.next(action_name, action_param)
        if res is not None:
            print(f"Success={success} {atm.state} {res}")
        else:
            print(f"Success={success} {atm.state}")
#-----------------------------------------------



#-----------------------------------------------
# hackerrank_python1
stea#-----------------------------------------------



#-----------------------------------------------
# heaps
import heapq
from bigtree import dataframe_to_tree_by_relation,print_tree
from treelib import Node,Tree
'''
T1 -5
T2 - 4
T3 - 7
T4 - 9
T5 - 2
T6 - 6
'''

data = [10,20,43,1,2,65,17,44,2,3,1]
heapq.heapify(data)
def par_chil_dict(heap):
    temp=[f'{val} ind({i})' for i,val in enumerate(heap)]
    dct={}
    for i in range(len(temp)):
        dct[temp[i]]=[temp[2*i+1],temp[2*i+2]]
        if (2*i+2) == len(temp)-1:
            break
    return dct
tree_dct=par_chil_dict(data)
# print(tree_dct)
import pandas as pd
df=pd.DataFrame(columns=['child','parent'])
count=0
for i,val in tree_dct.items():
    for x in val:
        y=str(x)
        df.loc[len(df)]=[str(x),str(i)]
root=dataframe_to_tree_by_relation(df)
print(data)
print_tree(root)#-----------------------------------------------



#-----------------------------------------------
# inordertraversal
import ast
import bigtree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res


class solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        def inord(root):
            if root is None:
                return
            stack.append(root.val)
            inord(root.left)
            res.append(stack.pop(-1))
            inord(root.right)
        inord(root)
        return res
in_list=ast.literal_eval(input())
root=TreeNode(val=in_list[0])
cur_node=root
for x,i in enumerate(in_list[1:]):
    if i is not None:
        cur_node.left=TreeNode(val=i)
        cur_node=cur_node.left
    else:
        cur_node.right=in_list[x+1]
        continue
print(inorderTraversal(root))#-----------------------------------------------



#-----------------------------------------------
# insertposition
import ast
nums=ast.literal_eval(input())
target=ast.literal_eval(input())
def searchInsert(nums,target):
    L,R=0,len(nums)-1
    while L<=R:
        mid=(L+R)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            L=mid+1
        else:
            R=mid-1
    return L
    # counter=0
    # for i in nums:
    #     if i==target:
    #         return counter
    #     elif i>target:
    #         return counter
    #     counter+=1
    # return counter
result=searchInsert(nums,target)
print(result)#-----------------------------------------------



#-----------------------------------------------
# issametree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # elif not p or not q or p.val!=q.val:
        #     return False
        # return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        return self.pre(p)==self.pre(q)
    def pre(self,root):
        if not root:
            return [None]
        else:
            return [root.val]+self.pre(root.left)+self.pre(root.right)
        #-----------------------------------------------



#-----------------------------------------------
# is_subsequence
def isSubsequence(self, s: str, t: str) -> bool:
    # s_list=list(s)
    # t_list=list(t)
    # for i in s_list:
    #     if t_list[0]==i:
    #         t_list.pop(0)
    # return not t_list
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i + 1 :]
    return True
print(isSubsequence())
#-----------------------------------------------



#-----------------------------------------------
# k_frequentelements
from time import time
import numpy as np
import heapq
arr=np.random.randint(0,1000,10000000)
def timeit(func):
    def wrapper(*args, **kwargs):
        start=time()
        result = func(*args, **kwargs)
        print(f'{round(time()-start,2)} seconds - {func.__name__}') 
        return result
    return wrapper
class Solution:
    def freq_mapper(self,arr):
        count_map={}
        for i in arr:
            count_map[i]=1+count_map.get(i,0)
        return count_map
    @timeit
    def k_freq_by_count(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        result=list(set(arr))
        result.sort(key=lambda x:count_map[x],reverse=True)
        return 
    @timeit
    def k_freq_by_count_heap_max(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        heapq.nlargest(k,count_map.keys(),count_map.get)
        return 
    @timeit
    def k_freq_by_count_heap_min(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        min_heap=[]
        for num,count in count_map.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result = [i for _,i in min_heap]
        return 
    @timeit
    def k_freq_bucket_sort(self,arr,k=100):
        count_map=self.freq_mapper(arr)
        bucket_map={i:[] for i in range(len(arr)+1)}
        for num,count in count_map.items():
            bucket_map[count].append(num)
        result=[]
        for i in range(len(arr),0,-1):
            for num in  bucket_map[i]:
                result.append(num)
                if len(result)==k:
                    return
        return

Solution().k_freq_by_count(arr)
Solution().k_freq_by_count_heap_max(arr)
Solution().k_freq_by_count_heap_min(arr)
Solution().k_freq_bucket_sort(arr)#-----------------------------------------------



#-----------------------------------------------
# largestnumber
import ast
from functools import cmp_to_key
lst=ast.literal_eval(input())
class Solution:
    def largestNumber(self, nums) -> str:
        nums=[str(i) for i in nums]
        def comp(a,b):
            if a+b<b+a:
                return 1
            else:
                return -1
        lst=sorted(nums,key=cmp_to_key(comp))
        return str(int(''.join(str(i) for i in lst)))
print(Solution().largestNumber(nums=lst))#-----------------------------------------------



#-----------------------------------------------
# laststoneweight
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

            

            


#-----------------------------------------------



#-----------------------------------------------
# LASTWORDLENGHT
import ast
input=input()
def lgt(input):
    result=0
    while input[-1]==" ":
        input=input[:-1]
    if input=="":
        return 0
    while input[-1]!=" ":
        result+=1
        input=input[:-1]
        if input=="":
            return result
    return result
print(lgt(input))
    
#-----------------------------------------------



#-----------------------------------------------
# leet1
temp=dict(
I = 1,
V = 5,
X = 10,
L = 50,
C = 100,
D = 500,
M = 1000)
class Solution:
    s=input().replace("\"","")
    def roman(self,s:str) -> int:
        output=0
        i=0
        while i < len(s):
            x=temp[s[i]]
            if i!=len(s)-1:
                if ((s[i+1]=='V' or s[i+1]=='X') and (s[i]=='I'))| \
                    ((s[i+1]=='L' or s[i+1]=='C') and (s[i]=='X'))| \
                    ((s[i+1]=='D' or s[i+1]=='M') and (s[i]=='C')):
                    x=temp[s[i+1]]-temp[s[i]]
                    i+=1
            output=output+x
            i+=1
        return output
    print(roman(input().replace("\"","")))
#-----------------------------------------------



#-----------------------------------------------
# leet2
def longestCommonPrefix(strs):
    if len(strs)==1:
        return strs[0]
    strs_nums=[]
    for i in range(0,len(strs)):
        strs_nums.append(len(strs[i]))
    min_str=strs[strs_nums.index(min(strs_nums))]
    x=list(min_str)
    if len(x)==0:
        return ""
    output=""
    i=0
    for letter in x:
        for p,each_word in enumerate(strs):
            if letter==each_word[i]:
                if p==len(strs)-1:
                    output=output+letter
            else:
                return output
        i+=1
    return output

print(longestCommonPrefix(input().split(",")))
        #-----------------------------------------------



#-----------------------------------------------
# LINKEDLISTS
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = None
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None    
    def append(self,data):
        new_node=Node(data,self.head)
        self.head=Node

        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list=LinkedList()
my_list.display()












# llist=LinkedList()
# first_node=Node('a')
# llist.head=first_node
# second_node=Node('b')
# third_node=Node('c')
# first_node.next=second_node
# second_node.next=third_node
# llist#-----------------------------------------------



#-----------------------------------------------
# longestcommonprefix
def LONGESTCOMMONPREFIX(x) -> str:
    

    return x
x=list(map(str,input().split(',')))
print(LONGESTCOMMONPREFIX(x))#-----------------------------------------------



#-----------------------------------------------
# max_avg_subarray1
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        result = sum(nums[:k])
        max_sum = result
        for i in range(k, len(nums)):
            result += nums[i] - nums[i - k]
            max_sum = max(max_sum, result)
        return max_sum / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
#-----------------------------------------------



#-----------------------------------------------
# max_profit
"""
FIND THE LARGEST PROFIT POSSIBLE IN A LIST 

in cases like this, 
use two pointers, but the key is to move the lp to the current rp 
because we have already found the max from the past lp to current rp
so this makes the code efficient.

"""


class Solution:
    def maxProfit(self, lst: List[int]) -> int:
        lp, rp, max_profit = 0, 1, 0
        while rp < len(lst):
            if lst[lp] < lst[rp]:
                cur_profit = lst[rp] - lst[lp]
                max_profit = max(cur_profit, max_profit)
            else:
                lp = rp
            rp += 1
        return max_profit
#-----------------------------------------------



#-----------------------------------------------
# mergesortedarray
import ast
def merge(L1,L2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(L1)==1:
        if L1[0]==0:
            L1[0]=L2[0]
        else:
            L1
    else:
        ln=len(L1)
        for i in range(ln-1,-1,-1):
            if L1[i]!=0 or len(L2)==0:
                break
            L1[i]=L2[-1]
            L2.pop(-1)
        L1.sort()
        print(L1)
L1=ast.literal_eval(input())
L2=ast.literal_eval(input())
merge(L1,L2)#-----------------------------------------------



#-----------------------------------------------
# mergesortedlist
import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
L1=ast.literal_eval(input())
L2=ast.literal_eval(input())
def build_nodelist(L1):
    LN=ListNode(val=L1[0])
    CURNODE=LN
    for i in L1[1:]:
        NEW_NODE=ListNode(val=i)
        CURNODE.next=NEW_NODE
        CURNODE=NEW_NODE
    return LN
LN1=build_nodelist(L1)
LN2=build_nodelist(L2)
def combine_nodes(LN1,LN2):
    C1,C2=LN1,LN2
    if C1.val<C2.val:
        RES=ListNode(val=C1.val)
        CURNODE=RES
        C1=C1.next
    elif C1.val==C2.val:
        RES=ListNode(val=C1.val)
        CURNODE=RES
        CURNODE.next=ListNode(val=C1.val)
        C1=C1.next
        C2=C2.next
    else:
        RES=ListNode(val=C2.val)
        C2=C2.next
    while C1 and C2 is not None:
        if C1.val<C2.val:
            CURNODE.next=ListNode(val=C1.val)
            C1=C1.next
        elif C1.val==C2.val:
            CURNODE.next=ListNode(val=C1.val)

            CURNODE.next.next=ListNode(val=C1.val)
            C1=C1.next
            C2=C2.next
        else:
            CURNODE=ListNode(val=C2.val)
            C2=C2.next
    return RES
curnode=combine_nodes(LN1,LN2)
RES_List=[]
while curnode is not None:
    RES_List.append(curnode.val)
    curnode=curnode.next
print(RES_List)

#-----------------------------------------------



#-----------------------------------------------
# MERGESORTEDLISTS
import ast
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def mergetwolists(x,y):
    if len(x)==0:
        return y
    elif len(y)==0:
        return x
    for position,i in enumerate(x):
        ListNode(val=i,next=x[position+1])



    return ListNode


x=ast.literal_eval(input())
y=ast.literal_eval(input())
print(mergetwolists(x,y))
#-----------------------------------------------



#-----------------------------------------------
# missingnum
import ast
class solution:
    def missingnum(self,nums):
       return [i for i in range(0,len(nums)+1) if i not in nums][0]
   
nums=ast.literal_eval(input())
print(solution().missingnum(nums=nums))#-----------------------------------------------



#-----------------------------------------------
# node_viewer
from pyvis import network
network1= network.Network(height=500,width=1000,notebook=True,directed=False)
network1.add_nodes(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
network1. add_edges([ ('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G'),('F','H'),('F','I')])
network1.show_buttons(filter_=['physics'])

network1.show('test.html')

network_llist= network.Network(height=500,width=1000,notebook=True,directed=False)
network_llist.add_nodes([1,2,3,4,5])
network_llist.add_edges([(1,2),(2,3),(3,4),(4,5)])
network_llist.show_buttons(filter_=['physics'])
network_llist.show('test1.html')#-----------------------------------------------



#-----------------------------------------------
# nth-uglynumber
n=int(input())
class Solution:
    def isUgly(self, n: int) -> bool:
        count=1
        val=1
        result=1
        while count<n+1:
            val=result
            for i in [2,3,5]:
                while val%i==0:
                    val//=i
            if val==1:
                 count+=1
                 result+=1
            else:
                result+=1
        return result-1
print(Solution().isUgly(n=n))#-----------------------------------------------



#-----------------------------------------------
# openclosebrackets
my_dict= {'(': ')', '{': '}', '[':']'}
def isvalid(x):
    i=0
    if len(x)%2!=0:
        return False
    List=[i for i in x]
    while i<len(List)-1:
        if List[i] in my_dict.keys():
            if my_dict[List[i]]==List[i+1]:
                del List[i:i+2]
                i=0
                if len(List)==0:
                    return True
            else:
                i+=1
        else:
            i+=1
    return False
    #     if my_dict[x[i]]==x[i+1]:
    #         i+=2
    #         continue
    #     else:
    #         return False
    # return True
x=input()
print(isvalid(x))#-----------------------------------------------



#-----------------------------------------------
# palindrome
def isPalindrome(num) -> bool:
    List=list(str(num))
    if List[0]=='-':
        return False
    ln=len(List)
    if len(List) % 2==0:
        return List[:ln//2]==List[ln//2:][::-1]
    else:
        return List[:ln//2]==List[ln//2+1:][::-1]
x=input()
print(isPalindrome(x))#-----------------------------------------------



#-----------------------------------------------
# PHONELETTERS
dict={2:('a','b','c'),
      3:('d','e','f'),
      4:('g','h','i'),
      5:('j','k','l'),
      6:('m','n','o'),
      7:('p','q','r','s'),
      8:('t','u','v'),
      9:('w','x','y','z'),}
def PHONELETTERS(digits):
    digits=digits.replace('1',"")
    digits=digits.replace('0',"")
    if digits=='':
        return []
    ar=[int(i) for i in digits]
    result=[]
    i=1
    temp=dict[ar[0]]
    while i<len(ar):
        for j in dict[ar[i]]:
            for k in range(0,len(temp)):
                result.append(temp[k]+j)
        if result!=[] and i<len(ar)-1:
            temp=result
            result=[]
            i+=1
            continue
        i+=1
    if result==[]:
        return list(temp)
    return result
digits=input()
print(PHONELETTERS(digits))#-----------------------------------------------



#-----------------------------------------------
# plusone
import ast
digits=ast.literal_eval(input())
def plusone(digits):
    if len(digits)==0:
        return [1]
    val=""
    for i in digits:
        val+=str(i)
    result=str(int(val)+1)
    return [int(i) for i in result]
print(plusone(digits))#-----------------------------------------------



#-----------------------------------------------
# pramp
def calc_drone_min_energy(route):
    if len(route) == 1:
        return 0
    z = []
    # O(n)
    for i in route:
        z.append(i[2])

    kWh = 0
    min_egy = float("inf")
    # O(n)
    for i in range(1, len(z)):
        kWh += z[i - 1] - z[i]
        min_egy = min(min_egy, kWh)
    return -min_egy if min_egy < 0 else 0


def absSort(arr):
    arr.sort(key=lambda x: (abs(x),-x))
    for r in range(1, len(arr)):
        if arr[r - 1] > arr[r] and arr[r - 1] + arr[r] == 0:
            arr[r - 1], arr[r] = arr[r], arr[r - 1]
    return arr


arr = [2, -7, -2, -2, 0]
print(absSort(arr))
#-----------------------------------------------



#-----------------------------------------------
# pramp2
def get_shortest_unique_substring(arr, str):
  arr_map={i:1 for i in arr}
  sub_map={}
  have,want=len(arr),0
  min_l=float('inf')
  l=0
  for r in range(len(str)):
    char=str[r]
    sub_map[char]=1+sub_map.get(char,0)
    if char in arr_map and arr_map[char]==sub_map[char]:
      want+=1
    while have==want:
      if r-l+1<min_l:
        sub_str=[l,r]
        min_l=r-l+1
      sub_map[str[l]]-=1
      l+=1
      if char in arr_map and arr_map[char]>sub_map[char]:
        have-=1
  return str[sub_str[0]:sub_str[1]+1] if min_l != float('inf') else ''
  
arr = ['x','y','z']
str = "xyyzyzyx"
print(get_shortest_unique_substring(arr,str))

#-----------------------------------------------



#-----------------------------------------------
# pramp_bst_key
##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def find_largest_smaller_key(self, num):
        cur_node = self.root
        res = [-float("inf")]

        def in_trav(cur_node):
            print(cur_node.key)
            if not cur_node:
                return
            if cur_node.key < num:
                res[0] = max(res[0], cur_node.key)
                in_trav(cur_node.right)
            else:
                in_trav(cur_node.left)

        in_trav(cur_node)
        return res[0] if res[0] != -float("inf") else -1

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while currentNode is not None:
            if key < currentNode.key:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(17)

print("Largest smaller number is %d " % (result))
#-----------------------------------------------



#-----------------------------------------------
# remove_duplicates
import ast
in_list=ast.literal_eval(input())
def removeDuplicates(L):
    k=0
    if len(L)==0:
        return k
    else:
        counter=[]
        counter.append(L[0])
        while k<len(L)-1:
            if L[k]!=L[k+1]:
                counter.append(L[k+1])
            k+=1
    return counter
k=removeDuplicates(in_list)
print(k)#-----------------------------------------------



#-----------------------------------------------
# remove_element
import ast
lst=ast.literal_eval(input())
val=ast.literal_eval(input())
def remove_val(lst,val):
    result=[]
    for i in lst:
        if i!=val:
            result.append(i)
    return result
result=remove_val(lst,val)
print(result)#-----------------------------------------------



#-----------------------------------------------
# repeateddna
s=input()
class Solution:
    def repdna(self,s:str):
        hash={}
        for i in range(0,len(s)-9):
            sub=s[i:i+10]
            hash[sub]=hash.get(sub,0)+1
        return [i for i in hash.keys() if hash[i]>1]
        # lst=[s[i:i+10] for i in range(0,len(s)-9)]
        # return list(set([x for x in lst if lst.count(x)>1]))
        
print(Solution().repdna(s=s))#-----------------------------------------------



#-----------------------------------------------
# reverse_vowels
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        input_list = list(s)
        to_reverse = []
        for i, val in enumerate(input_list):
            if val.lower() in vowels:
                input_list[i] = ""
                to_reverse.append(val)
        for i, val in enumerate(input_list):
            if val == "":
                input_list[i] = to_reverse.pop()
        return "".join(input_list)
#-----------------------------------------------



#-----------------------------------------------
# romantoint
my_dict={'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000,
'IV':4,'IX':9,
'XL':40,'XC':90,
'CD':400,'CM':900}
def romantoint(num) -> int:
    List=list(num)
    x=len(List)
    i=0
    while  i<len(List)-1:
        if List[i]+List[i+1] in my_dict.keys():
            List[i]=List[i]+List[i+1]
            List.pop(i+1)
        i+=1
    return sum(my_dict[v] for v in List)
x=input()
print(romantoint(x))#-----------------------------------------------



#-----------------------------------------------
# sameleaves_bi_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        return_list1 = []
        return_list2 = []

        def leaf(root, arr):
            if root:
                leaf(root.left, arr)
                if root.left is None and root.right is None:
                    arr.append(root.val)
                leaf(root.right, arr)

        leaf(root1, return_list1)
        leaf(root2, return_list2)
        return return_list1 == return_list2
#-----------------------------------------------



#-----------------------------------------------
# sandbox
lst=[1,2,1,3]
dct={1:'a',2:'b'}
print([dct.keys()])#-----------------------------------------------



#-----------------------------------------------
# sherlock_anagrams
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    counter_map=Counter(s)
    for i in range(2,len(s)):
        sub_str=s[0:i]
        counter_map[''.join(sorted(sub_str))]+=1
        for j in range(1,len(s)):
            if i+j<=len(s):
                counter_map[''.join(sorted(s[j:j+i]))]+=1
    result=0
    for val in counter_map.values():
        result+=val*(val-1)//2
    return result

print(sherlockAndAnagrams('aacbbc'))#-----------------------------------------------



#-----------------------------------------------
# smallest_substringwindow
arr = ["x", "y", "z"]
str = "xyyzyzyx"


class Solution:
    def min_window(self, arr, str):
        if not str:
            return ""
        count_map = {}
        for i in arr:
            count_map[i] = 1 + count_map.get(i, 0)
        s_map = {}
        have, need = 0, len(count_map)
        l = 0
        res_len = float("infinity")
        for r in range(len(str)):
            char = str[r]
            s_map[char] = 1 + count_map(char, 0)
            if char in count_map and s_map[char] == count_map[char]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                s_map[str[l]] -= 1
                if str[l] in count_map and s_map[char] < count_map[char]:
                    have = -1
                l += 1

        return str[res[0], res[1] + 1] if res_len != float("infinity") else ""


print(Solution().min_window(arr, str))
#-----------------------------------------------



#-----------------------------------------------
# string_winner
def minion_game(string):
    vowels= ['A','E','I','O','U']
    KEVIN,STUART=0,0
    for i,val in enumerate(string):
        if val in vowels: KEVIN+=len(string)-i
        else: STUART+=len(string)-i
        
    if KEVIN>STUART:
        return print(f"Kevin {KEVIN}")
    elif KEVIN<STUART:
        return print(f"Stuart {STUART}")
    else:
        return print('Draw')

minion_game('BANANA')

# if __name__ == '__main__':
    # s = input()
    # minion_game(s)#-----------------------------------------------



#-----------------------------------------------
# summary_builder
import os
from glob import glob

lst = glob("./*.py", root_dir=None)
lst = [i for i in lst if "leets_summary" not in i]
with open("leets_summary.py", "w") as f2:
    for i in lst:
        with open(i, "r") as f:
            content = f.read()
            f2.write("#-----------------------------------------------\n")
            f2.write(f"# {os.path.basename(i).rsplit('.',1)[0]}\n")
            f2.write(content)
            f2.write("#-----------------------------------------------\n")
            f2.write("\n\n\n")
with open("leets_summary.py", "r") as f2:
    print(f2.read())
#-----------------------------------------------



#-----------------------------------------------
# time_decorator
from time import time
import sys
sys.set_int_max_str_digits(500)
def timer(func):
    def wrapper(*args, **kwargs):
        start=time()
        print(f"started {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result=func(*args, **kwargs)
        print(f"Total time: {round(time()-start,2)} Seconds")
        print(f"result: {result}")
    return wrapper

@timer
def multiplier(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result
x=10

multiplier(x)
    #-----------------------------------------------



#-----------------------------------------------
# trie_class
from dataclasses import dataclass,field
from typing import Dict,List

@dataclass
class directory_node:
    folder: Dict[str,'directory_node'] = field(default_factory=dict)
    files: List[str] = field(default_factory=list)

    def insert_folder(self,folder_path:str) -> None:
        node=self
        for folder_name in folder_path:
            if folder_name not in node.folder:
                node.folder[folder_name]=directory_node()
            node=node.folder[folder_name]
    def insert_file(self,folder_path:str,file_name:str) -> None:
        node=self
        for folder_name in folder_path:
            if folder_name not in node.folder:
                node.folder[folder_name]=directory_node()
            node=node.folder[folder_name]
        node.files.append(file_name)
    def print_directory(self,node=None,indent=0):
        if not node:
            return
        for folder_name,child_node in node.folder.items():
            print("  "*indent +f"-{folder_name}")
            self.print_directory(child_node,indent+1)
            for file_name in child_node.files:
                print("  "*(indent+1)+f"-{file_name}")
            
""" INITIALIZE THE TRIE"""                
trie=directory_node()

""" PROCESS THE FILE PATHS AND CREATE THE FOLDER STRUCTURE"""
file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/jack/diary/2023-04-03.txt"
]

for file_path in file_paths:
    tokens=file_path.split("/")
    path_list=tokens[1:-1]
    file_name=tokens[-1]
    trie.insert_folder(path_list)
    trie.insert_file(path_list,file_name)
trie.print_directory(trie)
    
    
    
        
            
        
        
        
    
    #-----------------------------------------------



#-----------------------------------------------
# two-sum_binary
x = 3
y = 4
x_bin=bin(x)[2:]
y_bin=bin(y)[2:]
max_len=max(len(x_bin),len(y_bin))
x_bin=x_bin.zfill(max_len)
y_bin=y_bin.zfill(max_len)
result=""
carry=0
for i in range(max_len-1,-1,-1):
    r=carry
    r+=1 if x_bin[i]=="1" else 0
    r+=1 if y_bin[i]=="1" else 0
    result= ('1' if r%2==1 else '0')+result
    carry=0 if r<2 else 1
if carry!=0:
    result='1'+result
print(int(result,2))#-----------------------------------------------



#-----------------------------------------------
# two_sum_leetcode1
# use hashmap when the problem statement has 'unique solution' available mentioned


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for indx, val in enumerate(nums):
            if target - val in hash_map:
                return [hash_map[target - val], indx]
            else:
                hash_map[val] = indx
#-----------------------------------------------



#-----------------------------------------------
# udem
import pyautogui as sim
import time
for i in range(1,4):
    sim.click(x=2776, y=1485) # video position
    time.sleep(3)
    sim.click(x=2845, y=851)  # next vid
    time.sleep(3)#-----------------------------------------------



#-----------------------------------------------
# ugly2
n=int(input())
class solution:
    def ugly2(self,n:int):
        dp=[0]*n
        i2=i3=i5=0
        dp[0]=1
        for i in range(1,n):
            next_dp=min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            dp[i]=next_dp
            if next_dp==dp[i2]*2:
                i2+=1
            if next_dp==dp[i3]*3:
                i3+=1
            if next_dp==dp[i5]*5:
                i5+=1
            # i2+=(1 if next_dp==dp[i2]*2 else 0)
            # i3+=(1 if next_dp==dp[i3]*3 else 0)
            # i5+=(1 if next_dp==dp[i2]*5 else 0)
        return dp[-1]
print(solution().ugly2(n=n))#-----------------------------------------------



#-----------------------------------------------
# uglynumber
n=int(input())
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<0:
            return False
        while n%2==0:
            n/=2
        while n%3==0:
            n/=3
        while n%5==0:
            n/=5
        if n==1:
            return True
        else:
            return False
print(Solution().isUgly(n=n))#-----------------------------------------------



#-----------------------------------------------
# unique_occurs
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hash_map={i:0 for i in arr}
        for i in arr:
            hash_map[i]+=1
        occur_list=[val for _,val in hash_map.items()]
        return list(set(occur_list))==occur_list
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))#-----------------------------------------------



#-----------------------------------------------
# validip
def validip(input_string):
    lst=input_string.split('.')
    if len(lst)!=4:
        return False
    lst = [int(i) if i.isdigit() else i for i in lst]
    if not all([isinstance(i,int) for i in lst]):
        return False
    if not all([int(i)>=0 and int(i)<=255 for i in lst]):
        return False
    return True

print(validip('255.23.12.23'))
print(validip('255.23.12.278'))
print(validip('255.23.12.-2'))
print(validip('255.23.12.2.12'))
print(validip('255.23.12. a'))#-----------------------------------------------



#-----------------------------------------------
# zllw
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
#-----------------------------------------------



