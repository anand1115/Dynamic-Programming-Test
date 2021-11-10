def memorization(weights,profits,space,n,memo={}):
    key="{}-{}".format(space,n)
    if key in memo:
        return memo[key]
    if(space<=0 or n<=0):
        return 0
    else:
        if(weights[n-1]>space):
            memo[key]=memorization(weights,profits,space,n-1)
            return memo[key]
        else:
            withoutitem=memorization(weights,profits,space,n-1)
            withitem=profits[n-1]+memorization(weights,profits,space-weights[n-1],n-1)
            memo[key]=max(withitem,withoutitem)
            return memo[key]

def tabulation(weights,profits,space,n):
    dp=[[-1 for j in range(space+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(space+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(weights[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(profits[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
    return dp[n][space]
                

weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
space=int(input())
print(memorization(weights,profits,space,len(weights)))
print(tabulation(weights,profits,space,len(weights)))
    
