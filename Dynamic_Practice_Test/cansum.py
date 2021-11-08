def cansum(target,mylist,memo={}):
    if target in memo:
        return memo[target]
    if(target==0):
        return True
    elif(target<0):
        return False
    else:
        for i in mylist:
            temp=mylist.copy()
            temp.remove(i)
            memo[target]=cansum(target-i,temp,memo)
            if(memo[target]):
                return True
        return False
target=int(input())
mylist=list(map(int,input().split()))
print(cansum(target,mylist))
