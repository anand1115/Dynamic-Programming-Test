#Find maximum sum of circular sub array
#input : 10 5 -5  -> sub arrays 10,5,-5,10 5,5 -5,10 5 -5,-5 10,-5 10 5. 
#output : 15
#location arr2/3rd
def method(arr):
    n=len(arr)
    final=arr[0]
    for i in range(n):
        current=arr[i]
        maximum=arr[i]        
        for j in range(1,n):
            index=(i+j)%n
            current+=arr[index]
            maximum=max(current,maximum)
        final=max(maximum,final)
    return final
arr=list(map(int,input().split()))
print(method(arr))
