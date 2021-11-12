def basic(target,mylist,n):
    if((n<=0 and target>0) or target<0):
        return float('inf')
    if(target==0):
        return 0
    else:
        exclude=basic(target,mylist,n-1)
        include=basic(target-mylist[n-1],mylist,n)
        return min(1+include,exclude)

def memorization(target,mylist,n):
    global memo
    key=str(target)+":"+str(n)
    if(key in memo):
        return memo[key]
    if((n<=0 and target>0) or (target<0)):
        return float('inf')
    if(target==0):
        return 0
    else:
        exclude=memorization(target,mylist,n-1)
        include=memorization(target-mylist[n-1],mylist,n)
        memo[key]=min(1+include,exclude)
        return memo[key]

def tabulation(target,mylist,n):
    dp=[[None for i in range(target+1)] for j in range(n+1)]
    for i in range(1,target+1):
        dp[0][i]=float('inf')
    for i in range(n+1):
        dp[i][0]=0
    for i in range(1,n+1):
        for j in range(1,target+1):
            if(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-mylist[i-1]])
    return dp[n][target]

def best_sum(target,mylist):
    global memo
    if target in memo:
        return memo[target]
    if target<0:
        return None
    if target==0:
        return []
    else:
        best=None
        for i in mylist:
            temp=best_sum(target-i,mylist)
            if(temp is not None):
                temp=[i]+temp
                if(best is not None and len(best)>len(temp)):
                    best=temp
                else:
                    best=temp
        memo[target]=best
        return best

target=int(input())
mylist=list(map(int,input().split()))
n=len(mylist)
print(basic(target,mylist,n))
memo={}
print(memorization(target,mylist,n))
print(tabulation(target,mylist,n))
memo={}
print(best_sum(target,mylist))
