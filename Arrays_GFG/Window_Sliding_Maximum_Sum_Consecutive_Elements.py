#Maximum Sum of k consecutive elements
#input : arr=[1,8,30,-5,20,7] k=3
#output: 45  (30,-5,20)

def method1(arr,k):
    n=len(arr)
    maximum=-float("inf")
    current=0
    for i in range(k):
        current+=arr[i]
    maximum=max(maximum,current)
    for i in range(k,n):
        current+=arr[i]-arr[i-k]
        maximum=max(maximum,current)
    return maximum
arr=list(map(int,input().split()))
k=int(input())
print(method1(arr,k))
