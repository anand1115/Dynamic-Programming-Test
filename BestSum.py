def bestSum(target,mylist):
    best=None
    if(target==0):
        return []
    elif(target<0):
        return None
    else:
        for i in mylist:
            rem=target-i
            temp=bestSum(rem,mylist)
            if(temp is not None):
                bestComb=temp+[i]
                if(best is None or len(bestComb)<len(best)):
                    best=bestComb
        return best

def bestSum_Dynamic(target,mylist,memo={}):
    best=None
    if(target in memo):
        return memo[target]
    if(target==0):
        return []
    elif(target<0):
        return None
    else:
        for i in mylist:
            rem=target-i
            temp=bestSum_Dynamic(rem,mylist,memo)
            if(temp is not None):
                bestComb=temp+[i]
                if(best is None or len(bestComb)<len(best)):
                    best=bestComb
        memo[target]=best
        return memo[target]
print(bestSum_Dynamic(1000,[2,3,4,10]))
        
