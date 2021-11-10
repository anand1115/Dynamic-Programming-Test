memo={}
def cansum(target,mylist):
    global memo
    if(target in memo):
        return memo[target]
    if(target<0):
        return False
    if(target==0):
        return True
    else:
        for i in mylist:
            temp=cansum(target-i,mylist)
            if(temp==True):
                memo[target]=temp
                return memo[target]
        memo[target]=False
        return memo[target]
memo2={}
def howsum(target,mylist):
    global memo2
    if target in memo2:
        return memo2[target]
    if(target<0):
        return None
    if(target==0):
        return []
    else:
        for i in mylist:
            temp=howsum(target-i,mylist)
            if(temp!=None):
                memo2[target]=[i]+temp
                return memo2[target] 
        memo2[target]=None
        return None
memo3={}
def bestsum(target,mylist):
    best=None
    global memo3
    if target in memo3:
        return memo3[target]
    if target<0:
        return None
    if(target==0):
        return []
    else:
        for i in mylist:
            temp=bestsum(target-i,mylist)
            if(temp!=None):
                temp=[i]+temp
                if best is None:
                    best=temp
                elif(best is not None and len(best)>len(temp)):
                    best=temp
        memo3[target]=best
        return best


def allsum(target,mylist):
    if target<0:
        return None
    if target==0:
        return [[]]
    else:
        ways=[]
        for i in mylist:
            temp=allsum(target-i,mylist)
            if(temp!=None):
                for j in temp:
                    j.insert(0,i)
                    ways.append(j)
        return ways
                    
                    
                




target=int(input(("Enter Target : ")))
mylist=list(map(int,input().split()))
print(cansum(target,mylist))
print(howsum(target,mylist))
print(bestsum(target,mylist))
print(allsum(target,mylist))
    
