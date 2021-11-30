class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:

    def __init__(self):
        self.head=None


    def add_at_begin(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            self.head.next=self.head
        else:
            head=self.head
            node.next=head
            self.head=node
            temp=head
            while temp.next!=head:
                temp=temp.next
            temp.next=self.head

    def add_at_begin_eff(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            self.head.next=self.head
        else:
            temp=self.head.next
            self.head.next=node
            node.next=temp
            #swapping first two nodes data
            self.head.data=self.head.data^self.head.next.data
            self.head.next.data=self.head.next.data^self.head.data
            self.head.data=self.head.data^self.head.next.data
            #O(1) Solution

    def add_at_end(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head

    def add_at_end_eff(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.head.next=self.head
        else:
            temp=self.head.next
            self.head.next=node
            node.next=temp
            temp=self.head.data
            self.head.data=node.data
            node.data=temp
            self.head=node

    def delete_at_begin(self):
        if(self.head is None):
            return
        else:
            if(self.head.next==self.head):
                self.head=None
                return
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=temp.next.next
            self.head=temp.next

    def delete_at_begin_eff(self):
        if self.head is None:
            return
        else:
            if(self.head.next==self.head):
                self.head=None
                return
            self.head.data=self.head.next.data
            self.head.next=self.head.next.next

    def delete_at_end(self):
        if self.head is None:
            return
        else:
            if(self.head.next==self.head):
                self.head=None
            else:
                temp=self.head
                while temp.next.next!=self.head:
                    temp=temp.next
                temp.next=self.head
                return


    def delete_kth(self,k):
        if(self.head==None):
            return
        else:
            if(k==1):
                self.delete_at_begin_eff()
            else:
                count=1
                temp=self.head
                if(k==2):
                    temp.next=temp.next.next
                    return
                while count!=k-1:
                    temp=temp.next
                    count+=1
                temp.next=temp.next.next
                    
            
    def print(self):
        head=self.head
        if(head is None):
            print("Empty linked List ")
        else:
            temp=head
            while temp.next!=head:
                print(temp.data,end="-->")
                temp=temp.next
            print(temp.data)

k=Linked_List()
k.add_at_begin(10)
k.add_at_begin(20)
k.add_at_begin(30)
k.add_at_end(40)
k.add_at_end(50)
k.delete_at_begin()
k.delete_at_end()
k.delete_kth(3)
k.print()
s=Linked_List()
s.add_at_begin_eff(10)
s.add_at_begin_eff(20)
s.add_at_begin_eff(30)
s.add_at_end_eff(40)
s.add_at_end_eff(50)
s.delete_at_begin_eff()
s.print()

        
