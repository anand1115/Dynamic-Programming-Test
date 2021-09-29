def solve(m,n):
    if(m==0 or n==0):
        return 0
    elif(m==1 and n==1):
        return 1
    else:
        return solve(m,n-1)+solve(m-1,n)
def solve_dynamically(m,n,memo={}):
    key=str(m)+"-"+str(n)
    if(m==0 or n==0):
        return 0
    elif(m==1 or n==1):
        return 1
    elif(key in memo):
        return memo[key]
    else:
        memo[key]=solve_dynamically(m,n-1,memo)+solve_dynamically(m-1,n,memo)
        return memo[key]
print(solve_dynamically(180,180))
