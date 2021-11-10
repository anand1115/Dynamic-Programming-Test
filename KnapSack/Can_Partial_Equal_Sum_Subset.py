def CanPartion(target,mylist,n,dp):
    if(dp[n][target]!=None):
        return dp[n][target]
    if(target<0):
        return False
    if(target==0):
        return True
    if(n<=0):
        return False
    if(mylist[n-1]>target):
        dp[n][target]=CanPartion(target,mylist,n-1,dp)
        return dp[n][target] 
    else:
        dp[n][target]=CanPartion(target,mylist,n-1,dp) or CanPartion(target-mylist[n-1],mylist,n-1,dp)
        return dp[n][target]

def CanPart(target,mylist,n,dp):
    for i in range(n+1):
        for j in range(target+1):
            if(i==0 and j!=0):
                dp[i][j]=False
            elif(j==0):
                dp[i][j]=True
            elif(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-mylist[i-1]]
    return dp[n][target]



target=int(input())
mylist=list(map(int,input().split()))
dp=[[None for j in range(target+1)] for i in range(len(mylist)+1)]
if(sum(mylist) & 1):
    print(False)
else:
    print(CanPartion(target//2,mylist,len(mylist),dp))
    print(CanPart(target//2,mylist,len(mylist),dp))
