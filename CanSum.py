def cansum(target,mylist):
    if(target==0):
        return True
    elif(target<0):
        return False
    else:
        for i in mylist:
            if(cansum(target-i,mylist)):
                return True
        return False


def cansum_dynamic(target,mylist,memo={}):
    if(target==0):
        return True
    elif(target<0):
        return False
    elif(target in memo):
        return memo[target]
    else:
        for i in mylist:
            temp=target-i
            memo[temp]=cansum_dynamic(temp,mylist,memo)
            if(memo[temp]):
                return True
        return False
    
            

print(cansum_dynamic(300,[7,14]))
