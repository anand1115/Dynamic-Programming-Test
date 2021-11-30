n=int(input())
arr=list(map(int,input().split()))
final=0
water=0
temp=arr[0]
for i in range(1,n):
    if(arr[i]<temp):
        water+=(temp-arr[i])
    else:
        final+=water
        water=0
        temp=arr[i]
print(final)
