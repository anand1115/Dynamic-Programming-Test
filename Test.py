class Node:
    def __init__(self,key):
        self.key=key
        self.count=0
        self.locked=False
        self.parent=None

    def __repr__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.map={}

    def lock(self,node):
        if(node.locked or node.count!=0):
            return False
        else:
            temp=node.parent
            while temp:
                if(temp.locked):
                    return False
                temp=temp.parent
            node.locked=True
            temp=node.parent
            while temp:
                temp.count+=1
                temp=temp.parent
            return True

    def unlock(self,node):
        if not node.locked:
            return False
        else:
            temp=node.parent
            while temp:
                temp.count-=1
                temp=temp.parent
            node.locked=False
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
        print(tree.lock(tree.map[query[1]]))
    else:
        print(tree.unlock(tree.map[query[1]]))        
    for i in arr:
        print(i,"-->",i.count,'-->',i.locked)
