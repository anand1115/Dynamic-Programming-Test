def minimum(target,mylist,temp,n):
    if(n==0):
        return abs(((target-temp)-temp))
    else:
        return min(minimum(target,mylist,temp,n-1),minimum(target,mylist,temp+mylist[n-1],n-1))

def min_dp(mylist,n):
    mylistsum=sum(mylist)
    dp=[[None for j in range(mylistsum+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for j in range(1,mylistsum+1):
        dp[0][j]=False
    for i in range(n+1):
        for j in range(mylistsum+1):
            if(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-mylist[i-1]]
    for i in range(mylistsum//2,-1,-1):
        if(dp[n][i]):
            return (mylistsum-2*i)
    
mylist=list(map(int,input().split()))
target=sum(mylist)
temp=0
n=len(mylist)
print(minimum(target,mylist,temp,n))
print(min_dp(mylist,n))
