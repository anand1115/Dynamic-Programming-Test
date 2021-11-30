n=int(input())
arr=list(map(int,input().split()))
arr2=arr.copy()
d=int(input())
d=d%n
def rotate(arr):
    temp=arr[n-1]
    for i in range(n-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
for i in range(d):
    rotate(arr)
print(arr)
arr=arr2

