n=int(input())
arr=list(map(int,input().split()))
count=0
maxcount=0
for i in range(n):
    if(arr[i]==1):
        count+=1
    else:
        if(count>maxcount):
            maxcount=count
        count=0
else:
    if(count>maxcount):
        maxcount=count
print(maxcount)
