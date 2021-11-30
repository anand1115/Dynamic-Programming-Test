#####Not correct

###Don't forget to use the tail along with head


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Double_Linked_List:

    def __init__(self):
        self.head=None


    def length(self):
        count=0
        temp=self.head
        while temp:
            temp=temp.next
            count+=1
        return count

    def is_empty(self):
        return self.head==None

    def add(self,data):
        node=Node(data)
        if(self.is_empty()):
            self.head=node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node
        node.prev=temp

    def add_at_begin(self,data):
        node=Node(data)
        if(self.is_empty()):
            self.head=node
        else:
            temp=self.head
            self.head=node
            node.next=temp

    def find(self,data):
        if(self.is_empty()):
            return None
        else:
            temp=self.head
            while temp:
                if(temp.data==data):
                    return temp
                temp=temp.next
            return temp
        
    def add_after(self,index,data):
        node=Node(data)
        temp=self.find(index)
        if(temp):
            node.next=temp.next
            node.prev=temp
            temp.next=node
        else:
            print("Invalid index !!")

    def add_before(self,index,value):
        temp=self.find(index)
        node=Node(value)
        if(temp):
            if(temp.prev is None):
                self.head=node
                node.next=temp
                temp.prev=node
                return
            prev=temp.prev
            prev.next=node
            node.prev=prev
            node.next=temp
        else:
            print("Invalid Index")

    def delete(self,data):
        if(self.head==None):
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next:
                if(temp.data==data):
                    break
                temp=temp.next
            else:
                print("Node doesn't exist")
                return
            if(temp.prev is None):
                self.head=temp.next
                self.head.prev=None
            else:
                temp.prev.next=temp.next
                if(temp.next!=None):
                    temp.next.prev=temp.prev

    def print(self):
        temp=self.head
        while temp:
            print("<-",temp.data,end="->")
            temp=temp.next

k=Double_Linked_List()
k.print()
k.add(10)
k.add(20)
k.add(30)
k.add(40)
k.delete(10)
k.delete(30)
k.delete(40)
k.print()
        

    
