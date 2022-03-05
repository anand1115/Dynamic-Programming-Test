#Check Whether There is Subarry With Given Sum
#input :1 4 20 3 10 5 sum=30
#output :True

def method1(arr,sum):
    n=len(arr)
    for i in range(n):
        current=0
        for j in range(i,n):
            current+=arr[j]
        if(current==sum):
            return True
    return False

def method2(arr,sum):
    current=arr[0]
    left=0
    for right in range(1,len(arr)):
        while (current>sum and left<right-1):
            current-=arr[left]
            left+=1
        if(current==sum):
            return True
        if(right<len(arr)):
            current+=arr[right]
    while (current>sum and left<right-1):
            current-=arr[left]
            left+=1
    return current==sum


arr=list(map(int,input().split()))
sum=int(input())
print(method2(arr,sum))
            
