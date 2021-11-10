def countsum(target,mylist,n,memo):
    if(memo[n][target] is not None):
        return memo[n][target]
    if(target==0):
        return 1
    if(target<0):
        return 0
    if(n==0):
        return 0
    if(mylist[n-1]>target):
        memo[n][target]=countsum(target,mylist,n-1,memo)
        return memo[n][target]
    else:
        memo[n][target]=countsum(target,mylist,n-1,memo)+countsum(target-mylist[n-1],mylist,n-1,memo)
        return memo[n][target]

mylist=list(map(int,input().split()))
mylistsum=sum(mylist)
n=len(mylist)
diff=int(input())
target=(mylistsum+diff)//2
memo=[[None for j in range(target+1)] for i in range(n+1)]
print(countsum(target,mylist,n,memo))
