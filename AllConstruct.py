def AllConstruct(target,mylist):
    if(target==""):
        return [[]]
    else:
        ways=[]
        for i in mylist:
            if(target.startswith(i)):
                temp=AllConstruct(target[len(i):],mylist)
                for j in temp:
                    j.insert(0,i)
                ways.extend(temp)
        return ways
#not Working properly
def AllConstruct_Dynamic(target,mylist,memo={}):
    if target in memo:
        return memo[target]
    if(target==""):
        return [[]]
    else:
        ways=[]
        for i in mylist:
            if(target.startswith(i)):
                temp=AllConstruct_Dynamic(target[len(i):],mylist,memo)
                for j in temp:
                    j.insert(0,i)
                ways.extend(temp)
        #memo[target]=ways
        return ways
print(AllConstruct_Dynamic("Anandaaaaa",["A","a","n","and","an","d"]))
