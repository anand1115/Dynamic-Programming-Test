def CountSubset(target,mylist,n,memo):
    if(memo[n][target]!=None):
        return memo[n][target]
    if(target<0):
        return 0
    if(target==0):
        return 1
    if(n<=0):
        return 0
    if(mylist[n-1]>target):
        memo[n][target]=CountSubset(target,mylist,n-1,memo)
        return memo[n][target]
    else:
        memo[n][target]=CountSubset(target,mylist,n-1,memo)+CountSubset(target-mylist[n-1],mylist,n-1,memo)
        return memo[n][target]
def CountSub(target,mylist,n,dp):
    for i in range(n+1):
        for j in range(target+1):
            if(i==0 and j!=0):
                dp[i][j]=0
            elif(j==0):
                dp[i][j]=1
            elif(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-mylist[i-1]]
        print(dp)
    return dp[n][target]
target=int(input())
mylist=list(map(int,input().split()))
n=len(mylist)
dp=[[None for j in range(target+1)] for i in range(n+1)]
print(CountSubset(target,mylist,n,dp))
print(CountSub(target,mylist,n,dp))
