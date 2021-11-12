def basic(mylist,n,s1=0,s2=0):
    if(n==0):
        return abs(s1-s2)
    else:
        include=basic(mylist,n-1,s1+mylist[n-1],s2)
        exclude=basic(mylist,n-1,s1,s2+mylist[n-1])
        return min(include,exclude)

def memorization(mylist,n,s1=0,s2=0):
    global memo
    key=str(n)+":"+str(s1)
    if(key in memo):
        return memo[key]
    if(n==0):
        return abs(s1-s2)
    else:
        include=memorization(mylist,n-1,s1+mylist[n-1],s2)
        exclude=memorization(mylist,n-1,s1,s2+mylist[n-1])
        return min(include,exclude)

def tabulation(mylist,n):
    total_sum=sum(mylist)
    n=len(mylist)
    dp=[[None for j in range(total_sum+1)] for i in range(n+1)]
    for j in range(total_sum+1):
        dp[0][j]=False
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,total_sum+1):
            if(mylist[n-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-mylist[n-1]]
    print(dp)
    minimum=None
    for i in range(total_sum//2+1):
        if(dp[n][i]==True):
            minimum=(total_sum)-(2*i)
    return minimum
mylist=list(map(int,input().split()))
n=len(mylist)
print(basic(mylist,n))
memo={}
print(memorization(mylist,n))
print(tabulation(mylist,n))
