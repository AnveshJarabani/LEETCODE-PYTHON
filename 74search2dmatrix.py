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
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))