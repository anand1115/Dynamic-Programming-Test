def basic(target,mylist,n):
    if(target==0):
        return True
    if(target<0 or n<=0):
        return False
    if(mylist[n-1]>target):
        return basic(target,mylist,n-1)
    include=basic(target-mylist[n-1],mylist,n-1)
    exclude=basic(target,mylist,n-1)
    return include or exclude


def memorization(target,mylist,n):
    global memo
    if(memo[n][target]!=None):
        return memo[n][target]
    if(target==0):
        return True
    if(target<0 or n<=0):
        return False
    if(mylist[n-1]>target):
        memo[n][target]=memorization(target,mylist,n-1)
        return memo[n][target]
    include=memorization(target-mylist[n-1],mylist,n-1)
    exclude=memorization(target,mylist,n-1)
    memo[n][target]=(include or exclude)
    return memo[n][target]

def tabulation(target,mylist,n):
    dp=[[None for j in range(target+1)] for i in range(n+1)]
    for j in range(target+1):
        dp[0][j]=False
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-mylist[i-1]]
    return dp[n][target]
target=int(input())
mylist=list(map(int,input().split()))
n=len(mylist)
print(basic(target,mylist,n))
memo=[[None for j in range(target+1)] for i in range(n+1)]
print(memorization(target,mylist,n))
print(tabulation(target,mylist,n))

    
