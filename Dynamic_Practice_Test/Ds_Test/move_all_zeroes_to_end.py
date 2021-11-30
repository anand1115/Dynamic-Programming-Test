n=int(input())
arr=list(map(int,input().split()))
temp=[0]*n
count=0
for i in range(n):
    if(arr[i]!=0):
        temp[count]=arr[i]
        count+=1
print(*temp,sep=" ")
count=0
for i in range(n):
    if(arr[i]!=0):
        if(i==count):
            pass
        else:
            temp=arr[i]
            arr[i]=arr[count]
            arr[count]=temp
        count+=1
print(*arr,sep=" ")
