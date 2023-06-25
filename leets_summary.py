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
# 111
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
# 121
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
# 139
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
# 168
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
# 3SUM
def threeSum(nums):
    # if nums.count(0)==len(nums) and len(nums)>2:
    #     return [[0,0,0]]
    nums.sort()
    span=len(nums)
    k=0
    j,l=k+1,span-1
    lst=[]
    while (k<span-2):
        if j<l:
            sum=nums[k]+nums[j]+nums[l]
            if sum<0:
                while nums[j]==nums[j+1] and j<l-1:
                    j+=1
                j+=1
            elif sum>0:
                while nums[l]==nums[l-1] and j<l-1:
                    l-=1
                l-=1
            elif sum==0:
                lst.append([nums[k],nums[j],nums[l]])
                print([nums[k],nums[j],nums[l]]," K= ",k)
                while nums[j]==nums[j+1] and j<l-1:
                    j+=1
                j+=1
        else:
            while nums[k]==nums[k+1] and k<span-2:
                k+=1
            k+=1
            j,l=k+1,span-1
    return lst
print(threeSum(list(map(int,input().split(",")))))
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
# 3_longsubstring
class Solution:
    def lls(self,s):
        l,res=0,0
        char_set=set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[i])
            res=max(res,i-l+1)
        return res
print(Solution().lls(input()))  
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
# 463
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
# calculate
import pandas
import numpy as np
array=input()#-----------------------------------------------



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
            f2.write(f"# {os.path.basename(i).split('.')[0]}\n")
            f2.write(content)
            f2.write("#-----------------------------------------------\n")
            f2.write("\n\n\n")
with open("leets_summary.py", "r") as f2:
    print(f2.read())
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



