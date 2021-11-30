a=list(map(int,input().split()))
maxsum=-float('inf')
temp=a[0]
for i in range(1,len(a)):
    temp=max(a[i],a[i]+temp)
    if(temp>maxsum):
        maxsum=temp
print(maxsum)
