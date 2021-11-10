def count(coins,sum):
    if(sum<0):
        return None
    if(sum==0):
        return 1
    else:
        c=0
        for i in coins:
            temp=count(coins,sum-i)
            if(temp):
                c+=temp        
        return c
coins=list(map(int,input().split()))
sum=int(input())
print(count(coins,sum))
                
