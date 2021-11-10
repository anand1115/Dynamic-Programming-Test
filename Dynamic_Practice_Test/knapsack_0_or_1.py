def basic(wights,profits,n,w):
    if(n<=0):
        return 0
    if(w<=0):
        return 0
    if(wights[n-1]>w):
        return basic(weights,profits,n-1,w)
    exclude=basic(weights,profits,n-1,w)
    include=profits[n-1]+basic(weights,profits,n-1,w-weights[n-1])
    return max(exclude,include)
def memorization(weights,profits,n,w):
    global memo
    if(memo[n][w]!=None):
        return memo[n][w]
    if(n<=0):
        return 0
    if(w<=0):
        return 0
    if(weights[n-1]>w):
        memo[n][w]=memorization(weights,profits,n-1,w)
        return memo[n][w]
    exclude=memorization(weights,profits,n-1,w)
    include=profits[n-1]+memorization(weights,profits,n-1,w-weights[n-1])
    memo[n][w]=max(exclude,include)
    return memo[n][w]

def tabulation(weights,profits,n,w):
    dp=[[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if(i==0 or j==0):
               dp[i][j]=0
            elif(weights[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],profits[i-1]+dp[i-1][j-weights[i-1]])
    return dp[n][w]

weights=list(map(int,input("Please Enter weights : ").split()))
profits=list(map(int,input("Please Enter Profits : ").split()))
w=int(input("Please Enter total Weight : "))
n=len(weights)
print(basic(weights,profits,n,w))
memo=[[None for j in range(w+1)] for i in range(n+1)]
print(memorization(weights,profits,n,w))
print(tabulation(weights,profits,n,w))

            
        
    
    
    
