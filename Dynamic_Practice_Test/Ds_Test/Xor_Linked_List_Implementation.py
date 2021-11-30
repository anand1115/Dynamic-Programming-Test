import ctypes
class Node:
    def __init__(self,data):
        self.data=data
        self.npx=0

class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodes=[]

    def is_empty(self):
        return self.head==None

    def add(self,data):
        node=Node(data)
        if(self.is_empty()):
            self.head=node
            self.tail=node
        else:
            temp=self.tail
            temp.npx=(temp.npx)^(id(node))
            node.npx=(id(temp))
            self.tail=node
        self.nodes.append(node)

    def add_at_begin(self,data):
        node=Node(data)
        if(self.is_empty()):
            self.head=node
            self.tail=node
        else:
            self.head.npx=id(node)^(self.head.npx)
            node.npx=id(self.head)
            self.head=node
        self.nodes.append(node)

    def insert(self,index,data):
        prev=0
        temp=self.head
        while temp:
            if(temp.data==index):
                break
            k=id(temp)
            temp=self.get_next(temp,prev)
            prev=k
        else:
            print("Node Not Found")
            return
        node=Node(data)
        next=self.get_next(temp,prev)
        if(temp.npx == prev):
            self.add(data)
            return
        else:
            node.npx=id(temp)^id(next)
            next.npx=id(node)^(id(self.get_next(temp,next)))
            temp.npx=id(node)^prev
        self.nodes.append(node)
            
    
    def print(self):
        if(self.is_empty()):
            print("Empty Linked List !!")
        else:
            prev=0
            temp=self.head
            while temp:
                print("<-",temp.data,"->",end="")
                r=id(temp)
                temp=self.get_next(temp,prev)
                prev=r
    def get_next(self,node,prev):
        try:
            return ctypes.cast(node.npx^prev,ctypes.py_object).value
        except:
            return None

    def get_prev(self,node,next):
        try:
            return ctypes.cast(node.npx^next,ctypes.py_object).value
        except:
            return None


k=linked_list()
k.add(10)
k.add(20)
k.add(30)
k.add(40)
k.add_at_begin(5)
k.add(50)
k.add_at_begin(1)
k.insert(10,2)
k.print()
        
        
