k=list(map(int,input().split()))
n=len(k)
arr=k
count=0
maxcount=0
for i in range(n-1):
    if((arr[i]+arr[i+1])&1):
        count+=1
    else:
        maxcount=max(count,maxcount)
        count=0
else:
    maxcount=max(count,maxcount)
print(maxcount+1)
