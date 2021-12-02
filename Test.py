class Node:
    def __init__(self,key):
        self.key=key
        self.count=0
        self.locked=False
        self.parent=None
        self.locked_list={}
        self.locked_id=None

    def __repr__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.map={}

    def lock(self,node,uid):
        if(node.locked or node.count!=0):
            return False
        else:
            temp=node.parent
            while temp:
                if(temp.locked):
                    return False
                temp=temp.parent
            node.locked=True
            node.locked_id=uid
            temp=node.parent
            while temp:
                temp.count+=1
                temp.locked_list[id(node)]=node
                temp=temp.parent
            return True

    def unlock(self,node,uid):
        if not node.locked:
            return False
        elif(node.locked_id!=uid):
            return False
        else:
            temp=node.parent
            while temp:
                temp.count-=1
                del temp.locked_list[id(node)]
                temp=temp.parent
            node.locked=False
            node.locked_id=None
            return True

    def upgrade(self,node,uid):
        if(node.locked):
            return True
        temp=node.parent
        while temp:
            if(temp.locked):
                return False
            temp=temp.parent
        temp=list(node.locked_list.values()).copy()
        for i in temp:
            if(i.locked_id!=uid):
                return False
        for i in temp:
            self.unlock(i,uid)
        self.lock(node,uid)
        return True
                
        


n=int(input())
s=int(input())
tree=Tree()
arr=[]
m=0
j=0
for i in range(n):
    temp=input()
    node=Node(temp)
    arr.append(node)
    tree.map[temp]=node
    if(i==0):
        pass
    else:
        j+=1
        node.parent=arr[m]
        if(j==s):
            m+=1
            j=0
q=int(input())
for j in range(q):
    query=input().split()
    if(query[0]=='1'):
        print(tree.lock(tree.map[query[1]],query[2]))
    elif(query[0]=='2'):
        print(tree.unlock(tree.map[query[1]],query[2]))
    else:
        print(tree.upgrade(tree.map[query[1]],query[2]))
    
    for i in arr:
        print(i,"-->",i.count,'-->',i.locked,'-->',i.locked_list)
