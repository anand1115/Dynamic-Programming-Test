#left rotate an array by d positions
#input-1 2 3 4 5
#output-3 4 5 1 2

def method1(arr,d):
    temp=[0]*d
    for i in range(d):
        temp[i]=arr[i]
    count=0
    for j in range(d,len(arr)):
        arr[count]=arr[j]
        count+=1
    for i in range(d):
        arr[count]=temp[i]
        count+=1
    return arr

def rotate(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    print(arr,"check")
    return arr
def method2(arr,d):
    for i in range(d):
        arr=rotate(arr)
    return arr

def method3(arr,d):
    arr=arr[:d][::-1]+arr[d:][::-1]
    arr=arr[::-1]
    return arr

def reverse(arr):
    low=0
    high=len(arr)-1
    while low<high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr
    

arr=list(map(int,input().split()))
d=int(input())
#print(method1(arr,d))
#print(method2(arr,d))
#print(method3(arr,d))
print(reverse(arr))
    
