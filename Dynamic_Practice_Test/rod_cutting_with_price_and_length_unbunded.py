def basic(length,price,l,n):
    if(n<=0):
        return 0
    if(l<=0):
        return 0
    else:
        if(length[n-1]>l):
            return basic(length,price,l,n-1)
        include=price[n-1]+basic(length,price,l-length[n-1],n)
        exclude=basic(length,price,l,n-1)
        return max(include,exclude)

def memorization(length,price,l,n):
    key=f"{l}:{n}"
    global memo
    if key in memo:
        return memo[key]
    if(n<=0):
        return 0
    if(l<=0):
        return 0
    else:
        if(length[n-1]>l):
            memo[key]=basic(length,price,l,n-1)
            return memo[key]
        include=price[n-1]+memorization(length,price,l-length[n-1],n)
        exclude=memorization(length,price,l,n-1)
        memo[key]=max(include,exclude)
        return memo[key]

def tabulation(length,price,l,n):
    dp=[[None for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(length[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],price[i-1]+dp[i][j-length[i-1]])
    return dp[l][n]
l=int(input())
length=list(map(int,input().split()))
price=list(map(int,input().split()))
n=l
print(basic(length,price,l,n))
memo={}
print(memorization(length,price,l,n))
print(tabulation(length,price,l,n))

    
