def count(arr,n,sum):
    arr.sort()
    ans = 0
    for i in range(0,n-2):
        j=i+1
        k=n-1
        while(j<k):
            if(arr[i]+arr[j]+arr[k]>=sum):
                k=k-1
            else:
                ans+=(k - j)
                j=j+1
    return ans
arr=list(map(int,input().split()))
n=len(arr)
sum=int(input())
print(count(arr,n,sum))
