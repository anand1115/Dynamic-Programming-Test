#not understood go with unounded knapsack model


def basic(length,price):
    if(length<=0):
        return 0
    else:
        maxvalue=-float('inf')
        for i in range(1,length+1):
            cost=price[i-1]+basic(length-i,price)
            if(cost>maxvalue):
                maxvalue=cost
        return maxvalue

def tabulation(length,price):
    dp=[[0 for i in range(length+1)] for j in range(length+1)]
    for i in range(1,length+1):
        for j in range(1,length+1):
            dp[i][j]=max(dp[i-1][j],price[i-1]+dp[i][i-j])
    return dp[length][length]

length=int(input())
profit=list(map(int,input().split()))
print(basic(length,profit))
print(tabulation(length,profit))
        
