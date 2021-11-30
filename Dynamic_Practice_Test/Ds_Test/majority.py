arr=list(map(int,input().split()))
n=len(arr)
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i,v in count.items():
    if(v>n//2):
        print(i)
