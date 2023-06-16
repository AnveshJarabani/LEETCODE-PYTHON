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
print(coinchange(input,6249))