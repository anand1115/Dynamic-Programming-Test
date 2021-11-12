def basic(target,mylist,n):
    if(n<=0 or target<0):
        return 0
    if(target==0):
        return 1
    else:
        if(mylist[n-1]>target):
            return basic(target,mylist,n-1)
        else:
            return basic(target,mylist,n-1)+basic(target-mylist[n-1],mylist,n)

def memorization(target,mylist,n):
    global memo
    key=f"{target}-{n}"
    if key in memo:
        return memo[key]
    if(n<=0 or target<0):
        return 0
    if(target==0):
        return 1
    else:
        if(mylist[n-1]>target):
            memo[key]=memorization(target,mylist,n-1)
            return memo[key]
        else:
            memo[key]=memorization(target,mylist,n-1)+basic(target-mylist[n-1],mylist,n)
            return memo[key]

def tabulation(target,mylist,n):
    dp=[[None for i in range(target+1)] for j in range(n+1)]
    for i in range(target+1):
        dp[0][i]=0
    for j in range(n+1):
        dp[j][0]=1
    for i in range(1,n+1):
        for j in range(1,target+1):
            if(mylist[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-mylist[i-1]]
    return dp[n][target]


def count_sum(target,mylist):
    global memo
    if target in memo:
        return memo[target]
    if(target<0):
        return None
    if(target==0):
        return 1
    else:
        count=0
        for i in mylist:
            temp=count_sum(target-i,mylist)
            if(temp!=None):
                count+=temp
        memo[target]=count
        return count




target=int(input())
mylist=list(map(int,input().split()))
n=len(mylist)
print(basic(target,mylist,n))
memo={}
print(memorization(target,mylist,n))
print(tabulation(target,mylist,n))
memo={}
print(count_sum(target,mylist)) #not distinct ways
    
