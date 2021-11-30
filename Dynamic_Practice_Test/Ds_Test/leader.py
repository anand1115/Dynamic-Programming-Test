n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    temp=arr[i]
    flag=True
    for j in range(i+1,n):
        if(temp<=arr[j]):
            flag=False
    if flag:
        print(temp,end=" ")
print()
large=arr[-1]
print(large,end=" ")
for i in range(n-1,-1,-1):
    if(arr[i]>large):
        print(arr[i],end=" ")
        large=arr[i]
    
