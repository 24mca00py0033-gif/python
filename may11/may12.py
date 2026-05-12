class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoubleLinkedlist:
    def __init__(self):
        self.head=None
    
    def Insert_at_head(self,val):
        new_node=Node(val)
        
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
            
    def traverse_front(self):
        current=self.head
        while current:
            print(current.val,end=" ")
            current=current.next
        print()
    def traverse_backward(self):
        current=self.head
        while current.next:
            current=current.next
        while current:
            print(current.val,end=" ")
            current=current.prev
        print()
        
    def append_at_last(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
            
    def insert_at(self,val,position):
        new_node=Node(val)
        
        if position==0:
            self.Insert_at_head(val)
            return
        current=self.head
        count=0
        while current and count<position:
            current=current.next
            count+=1
            
        if current is None:
            print("position not found")
            return
        
        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node 
        
dll=DoubleLinkedlist()
dll.Insert_at_head(10)
dll.Insert_at_head(20)
dll.Insert_at_head(30)
dll.traverse_front()
dll.traverse_backward()
dll.append_at_last(40)
dll.traverse_front()
dll.insert_at(25,2)
dll.traverse_front()



        
            
    
        

        
            
        