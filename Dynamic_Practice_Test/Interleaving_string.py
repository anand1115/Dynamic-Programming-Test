def basic(a,a1,a2):
    if(len(a)==0 and len(a1)==0 and len(a2)==0):
        return True
    if(len(a)==0):
        return False
    x,y=False,False
    if(a1 and a[0]==a1[0]):
        x=basic(a[1:],a1[1:],a2)
    if(a2 and a[0]==a2[0]):
        x=basic(a[1:],a1,a2[1:])
    return x or y

def memorization(a,a1,a2):
    global memo
    key=(a,a1,a2)
    if key in memo:
        return memo[key]
    if(len(a)==0 and len(a1)==0 and len(a2)==0):
        return True
    if(len(a)==0):
        return False
    x,y=False,False
    if(a1 and a[0]==a1[0]):
        x=memorization(a[1:],a1[1:],a2)
    if(a2 and a[0]==a2[0]):
        x=memorization(a[1:],a1,a2[1:])
    memo[key]=x or y
    return memo[key]
a=input()
a1=input()
a2=input()
print(basic(a,a1,a2))
memo={}
print(memorization(a,a1,a2))

    
        
        
