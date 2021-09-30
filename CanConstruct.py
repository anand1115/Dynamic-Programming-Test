def canConstruct(target,mylist):
    if(target==""):
        return True
    else:
        for i in mylist:
            if(target.startswith(i)):
                temp=target[len(i):]
                if(canConstruct(temp,mylist)):
                    return True
        return False


def canConstruct(target,mylist,memo={}):
    if(target in memo):
        return memo[target]
    if(target==""):
        return True
    else:
        for i in mylist:
            if(target.startswith(i)):
                temp=target[len(i):]
                if(canConstruct(temp,mylist,memo)):
                    memo[target]=True
                    return True
        memo[target]=False
        return False
print(canConstruct("anand",["a","an","d"]))
