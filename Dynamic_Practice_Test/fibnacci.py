def fib2(n):
    if(n<=2):
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

def fib(n,memo):
    if memo[n]:
        return memo[n]
    else:
        if(n<=2):
            return 2
        else:
            memo[n]=fib(n-1,memo)+fib(n-1,memo)
        return memo[n]
n=int(input())
print(fib(n,[None]*(n+1)))
print(fib2(n))
