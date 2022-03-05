#Find the maximum length of maximum length of subarray.
#such that subarray should contain alternate even odd elements
#5 10 20 6 3 8
#o/p :3 -(6,3,8)

def method(arr):
    count=1
    final=1
    for i in range(1,len(arr)):
        if((arr[i]&1 and (not arr[i-1]&1)) or ((not arr[i]&1) and arr[i-1]&1)):
            count+=1
        else:
            final=max(final,count)
            count=1
    final=max(final,count)
    return final

arr=list(map(int,input().split()))
print(method(arr))
