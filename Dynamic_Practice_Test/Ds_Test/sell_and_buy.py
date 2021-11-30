n=int(input())
stock=list(map(int,input().split()))
profit=0
for i in range(1,n):
    if(stock[i]>stock[i-1]):
        profit+=(stock[i]-stock[i-1])
print(profit)
