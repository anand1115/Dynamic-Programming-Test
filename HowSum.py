def HowSum(target,mylist):
    if(target==0):
        return []
    elif(target<0):
        return None
    else:
        for i in mylist:
            temp=HowSum(target-i,mylist)
            if(temp is not None):
                return temp+[i]
        return None


def HowSum_Dynamic(target,mylist,memo={}):
    if(target==0):
        return []
    elif(target<0):
        return None
    elif(target in memo):
        return memo[target]
    else:
        for i in mylist:
            temp=target-i
            memo[temp]=HowSum_Dynamic(temp,mylist,memo)
            if(memo[temp] is not None):
                return memo[temp]+[i]
        return None

print(HowSum_Dynamic(300,[7,14]))
