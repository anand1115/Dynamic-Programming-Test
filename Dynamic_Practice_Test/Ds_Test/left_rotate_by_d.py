n=int(input())
arr=list(map(int,input().split()))
arr2=arr.copy()
arr3=arr.copy()
d=int(input())
d=d%n
def rotate(arr):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr
for i in range(d):
    rotate(arr)
print(arr)
arr=arr2
temp=[0]*d
for i in range(d):
    temp[i]=arr[i]
print("temporary array :",temp)
index=0
for j in range(d,n):
    arr[index]=arr[j]
    index+=1
i=0
while index<n:
    arr[index]=temp[i]
    i+=1
    index+=1
print(arr)
arr=arr3

def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def rotate(arr):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

rotate(arr)
print(arr)


    

