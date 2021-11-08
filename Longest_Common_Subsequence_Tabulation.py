def lcs(str1,str2):
    m=len(str1)+1
    n=len(str2)+1
    dp=[[None for i in range(n)] for i in range(m)]
    for i in range(m):
        dp[i][0]=0
    for j in range(n):
        dp[0][j]=0
    print(*[i for i in dp],sep="\n")
    for i in range(1,m):
        for j in range(1,n):
            if(str1[i-1]==str2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(*[i for i in dp],sep="\n")
    return dp[i][j]
print(lcs(input(),input()))
                
