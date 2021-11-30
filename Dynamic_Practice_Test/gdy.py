def tabulation(target,mylist,n):
    dp=[[None for j in range(target+1)] for i in range(n+1)]
    for j in range(target+1):
        dp[0][j]=0
    for i in range(n+1):
        dp[i][0]=1

    for i in range(1,n+1):
        for j in range(1,target+1):
            if(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-mylist[i-1]]
    return dp[n][target]

target=int(input())
n = 1000005
mylist=[]
prime = [True for i in range(n + 1)]
p = 2
c=0
M=100
import re
def isPrime(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None
while len(mylist) < target:
    mylist += filter(isPrime, range(M - 100, M)) 
    M += 100
n=len(mylist)
print(mylist[target])
print(tabulation(mylist[target-1],mylist,n))
