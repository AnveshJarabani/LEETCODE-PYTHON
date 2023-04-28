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
print(solution().ugly2(n=n))