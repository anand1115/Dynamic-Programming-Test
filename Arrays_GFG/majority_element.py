#find element which appears more than n/2 time in array
#input : 1 2 3 4 1 1 1
#output : -1
#location : arr2/4

def mymethod(arr):
    n=len(arr)
    temp={}
    for i in arr:
        if(i in temp):
            temp[i]+=1
        else:
            temp[i]=1
    for i,v in temp.items():
        if(v>n//2):
            return i
    return -1
def method1(arr):
    n=len(arr)
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                count+=1
        if(count>n//2):
            return arr[i]
    return -1

def method2(arr):
    n=len(arr)
    current=0
    count=1
    for i in range(1,n):
        if(arr[i]==arr[current]):
            count+=1
        else:
            count-=1
        if(count==0):
            current=i
            count=1
    count=0
    for i in range(n):
        if(arr[i]==arr[current]):
            count+=1
    if(count>n//2):
        return arr[current]
    return -1
            
            


arr=list(map(int,input().split()))
print(mymethod(arr))
print(method2(arr))
