def CountConstruct(target,mylist):
    if(target==""):
        return 1
    else:
        count=0
        for i in mylist:
            if(target.startswith(i)):
                count+=CountConstruct(target[len(i):],mylist)
        return count

def CountConstruct_Dynamic(target,mylist,memo={}):
    if(target in memo):
        return memo[target]
    if(target==""):
        return 1
    else:
        count=0
        for i in mylist:
            if(target.startswith(i)):
                suffix=target[len(i):]
                count+=CountConstruct_Dynamic(suffix,mylist,memo)
        memo[target]=count
        return count

print(CountConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",['e','ee','a']))
