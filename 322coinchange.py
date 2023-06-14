import ast
input=ast.literal_eval(input())
def coinchange(coins,amount):
    if amount==0:
        return 0
    coins.sort(reverse=True)
    count=0
    for n,coin in enumerate(coins):
        if n==len(coins)-1:
            if coin<=amount:
                count+=amount//coin
                amount %= coin
                if amount==0:
                    return count
                else:
                    return -1
            else:
                return -1
        count+=amount//coin
        amount%=coin
        if amount==0:
            return count
print(coinchange(input,6249))