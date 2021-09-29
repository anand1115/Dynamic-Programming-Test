def fib(n):
    if(n<=1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_dynamic(n,memo={}):
    if(n in memo):
        return memo[n]
    if(n<=1):
        return 1
    else:
        memo[n]=fib_dynamic(n-1,memo)+fib_dynamic(n-2,memo)
        return memo[n]
print(fib_dynamic(100))
