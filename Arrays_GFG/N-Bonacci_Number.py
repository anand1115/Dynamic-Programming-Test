#N-bonacci Number like fibanacci number
#input: n=3,m=8
#output:0 0 1 1 2 4 7 13
#input: n=4 m=10
#output:0 0 0 1 1 2 4 8 15 29

def method1(n,m):
    fib=[0]*n+[1]
    for i in range(m-n):
        fib.append(sum(fib[-4:]))
    return fib

n=int(input())
m=int(input())
print(fib(n,m))
        
