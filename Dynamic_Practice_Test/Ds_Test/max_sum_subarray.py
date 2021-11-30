k=list(map(int,input().split()))
n=len(k)
maxsum=0
for i in range(n):
    for j in range(i+1,n+1):
        if(sum(k[i:j])>maxsum):
            maxsum=sum(k[i:j])
print(maxsum)
arr=k
maxsum=-float('inf')
temp=arr[0]
for i in range(1,n):
    arr[i]=max(arr[i],arr[i]+temp)
    temp=arr[i]
    maxsum=max(temp,maxsum)
print(maxsum)
    
