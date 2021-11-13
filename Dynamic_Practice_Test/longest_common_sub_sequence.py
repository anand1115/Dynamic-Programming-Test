def basic(s1,s2,m,n):
    if(m==0 or n==0):
        return 0
    else:
        if(s1[m-1]==s2[n-1]):
            return 1+basic(s1,s2,m-1,n-1)
        else:
            exclude_s1=basic(s1,s2,m,n-1)
            exclude_s2=basic(s1,s2,m-1,n)
            return max(exclude_s1,exclude_s2)

def memorization(s1,s2,m,n):
    key=f"{m}-{n}"
    global memo
    if key in memo:
        return memo[key]
    if(m==0 or n==0):
        return 0
    else:
        if(s1[m-1]==s2[n-1]):
            memo[key]=1+memorization(s1,s2,m-1,n-1)
            return memo[key] 
        else:
            exclude_s1=memorization(s1,s2,m,n-1)
            exclude_s2=memorization(s1,s2,m-1,n)
            memo[key]=max(exclude_s1,exclude_s2)
            return memo[key]

def tabulation(s1,s2,m,n):
    dp=[[None for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


s1=input()
s2=input()
m=len(s1)
n=len(s2)
print(basic(s1,s2,m,n))
memo={}
print(memorization(s1,s2,m,n))
print(tabulation(s1,s2,m,n))

