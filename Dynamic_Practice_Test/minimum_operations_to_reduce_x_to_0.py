def basic(target,mylist,left,right,count=0):
    if(target<0):
        return float('inf')
    if(target==0):
        return count
    if(left>=len(mylist) and target>0):
        return float('inf')
    if(right<0 and target>0):
        return float('inf')
    left_move=basic(target-mylist[left],mylist,left+1,right,count+1)
    right_move=basic(target-mylist[right],mylist,left,right-1,count+1)
    return min(left_move,right_move)

def memorization(target,mylist,left,right,count=0):
    key=f"{left}-{right}-{count}"
    global memo
    if key in memo:
        return memo[key]
    if(target==0):
        return count
    if(target<0):
        return float('inf')
    if(left>=len(mylist) and target>0):
        return float('inf')
    if(right<0 and target>0):
        return float('inf')
    left_move=memorization(target-mylist[left],mylist,left+1,right,count+1)
    right_move=memorization(target-mylist[right],mylist,left,right-1,count+1)
    memo[key]=min(left_move,right_move)
    return memo[key]

target=int(input())
mylist=list(map(int,input().split()))
left=0
right=len(mylist)-1
print(basic(target,mylist,left,right))
memo={}
print(memorization(target,mylist,left,right))
