def max_sum(a):
    n=len(a)
    temp=a[0]
    maxsum=-float('inf')
    for i in range(1,n):
        temp=max(a[i],a[i]+temp)
        maxsum=max(maxsum,temp)
    return maxsum

def min_sum(arr):
    n=len(arr)
    temp=arr[0]
    minsum=float('inf')
    for i in range(1,n):
        temp=min(arr[i],arr[i]+temp)
        minsum=min(temp,minsum)
    return minsum

def min_sum_circular(arr):
    n=len(arr)
    maxsum=max_sum(arr)
    total=sum(arr)
    minsum=min_sum(arr)
    if(maxsum<0):
        return maxsum
    else:
        return max(maxsum,total-minsum)

print(min_sum_circular(list(map(int,input().split()))))
