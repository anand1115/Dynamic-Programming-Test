n=int(input())
arr=list(map(int,input().split()))
temp=-float('inf')
for i in range(n):
    for j in range(i+1,n):
        temp=max(temp,(arr[j]-arr[i]))
print(temp)

tempmin=arr[0]
large=-float('inf')
for i in range(1,n):
    tempmin=min(tempmin,arr[i])
    large=max(large,(arr[i]-tempmin))
print(large)
    
