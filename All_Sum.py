def allways(target,mylist):
    if(target<0):
        return False
    if(target==0):
        return [[]]
    else:
        ways=[]
        for i in mylist:
            temp=allways(target-i,mylist)
            if(temp!=False):
                for j in temp:
                    j.insert(0,i)
                ways.extend(temp)
        return ways

def allways_dynamic(target,mylist,memo={}):
    if target in memo:
        return memo[target]
    if(target<0):
        return False
    if(target==0):
        return [[]]
    else:
        ways=[]
        for i in mylist:
            temp=allways_dynamic(target-i,mylist,memo)
            if(temp!=False):
                for j in temp:
                    j.insert(0,i)
                ways.extend(temp)
        memo[target]=ways
        return memo[target]
    
print(allways_dynamic(int(input()),list(map(int,input().split()))))
