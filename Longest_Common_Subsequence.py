def lcs(s1,s2,m,n):
    if(m==0 or n==0):
        return 0
    if(s1[m-1]==s2[n-1]):
        return 1+lcs(s1,s2,m-1,n-1)
    else:
        return max(lcs(s1,s2,m,n-1),lcs(s1,s2,m-1,n))

def lcs_dynamic(s1,s2,m,n,memo={}):
    key=str(m)+":"+str(n)
    if(key in memo):
        return memo[key]
    else:
        if(m==0 or n==0):
            return 0
        if(s1[m-1]==s2[n-1]):
            memo[key]=1+lcs_dynamic(s1,s2,m-1,n-1,memo)
            return memo[key]
        else:
            memo[key]=max(lcs_dynamic(s1,s2,m,n-1,memo),lcs_dynamic(s1,s2,m-1,n,memo))
            return memo[key]
s1=input()
s2=input()
print(lcs_dynamic(s1,s2,len(s1),len(s2)))
