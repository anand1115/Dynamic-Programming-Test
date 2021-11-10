def issubset(target,mylist,n,memo={}):
    key="{}-{}".format(target,n)
    if key in memo:
        return memo[key]
    if(target<0 or n<0):
        return False
    if(target==0):
        return True
    if(mylist[n-1]>target):
        return issubset(target,mylist,n-1)
    else:
        memo[key]=issubset(target,mylist,n-1) or issubset(target-mylist[n-1],mylist,n-1)
        return memo[key]

def issub(target,mylist,n):
    dp=[[False for j in range(target+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if(j==0):
                dp[i][j]=True
            elif(i==0 and j!=0):
                dp[i][j]=False
            else:
                if(mylist[i-1]>target):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-mylist[i-1]]
    return dp[n][target]
                
target=int(input())
mylist=list(map(int,input().split()))
print(issubset(target,mylist,len(mylist)))
print(issub(target,mylist,len(mylist)))
