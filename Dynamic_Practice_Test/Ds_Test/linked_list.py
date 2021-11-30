class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def add(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node
    def add_at_begin(self,data):
        node=Node(data)
        if(self.is_empty()):
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def add_after_node(self,node,data):
        temp=node.next
        node.next=Node(data)
        node.next.next=temp


    def find_node(self,data):
        temp=self.head
        while temp:
            if(temp.data==data):
                return temp
            temp=temp.next
        return None
    def find_prev_node(self,data):
        temp=self.head
        while temp.next:
            if(temp.next.data==data):
                return temp
            temp=temp.next
        return None
        
    def add_after(self,index,data):
        temp=self.find_node(index)
        if(temp):
            self.add_after_node(temp,data)
        else:
            print("node doesn't exist")

    def add_before(self,index,data):
        if(self.head.data==index):
            self.add_at_begin(data)
            return
        temp=self.find_prev_node(index)
        if(temp):
            self.add_after_node(temp,data)
        else:
            print("node doesn't exist")

    def delete(self,data):
        if(self.head.data==data):
            self.head=self.head.next
        else:
            temp=self.find_prev_node(data)
            temp.next=temp.next.next
    
    def print(self):
        if(self.is_empty()):
            print("Linked list is Empty")
        else:
            temp=self.head
            while temp.next:
                print(temp.data,end="->")
                temp=temp.next
            print(temp.data)

k=linked_list()
k.add(10)
k.add(20)
k.add(30)
k.add_at_begin(40)
k.add_at_begin(50)
k.add_after(10,100)
k.add_before(10,1000)
k.add_before(50,10000)
k.add_after(30,10000000)
k.add_before(30,1.3)
k.delete(1.3)
k.delete(10000)
k.print()
                
            
