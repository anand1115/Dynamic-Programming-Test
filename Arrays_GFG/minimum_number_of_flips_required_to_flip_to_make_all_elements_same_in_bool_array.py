#minimum number of flips required to make all elements in array same
#we can alter either 0 or 1
#we can alter subequent elements at a time
#input : 1 1 0 0 0 1 1 0 1 0 0 0 1
#output : 3 (by altering 0 to 1)

def mymethod(arr):
    n=len(arr)
    temp={0:0,1:0}
    for i in range(1,n):
        if(arr[i-1]!=arr[i]):
            temp[arr[i-1]]+=1
    temp[arr[n-1]]+=1
    return min(list(temp.items()),key=lambda x:x[1])[1]
arr=list(map(int,input().split()))
print(mymethod(arr))
    
