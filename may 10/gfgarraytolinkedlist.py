# creating single linked list

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# node1=Node(5)
# node2=Node(10)
# node3=Node(15)
# node4=Node(20)

# node1.next=node2
# node2.next=node3    
# node3.next=node4

# print(node1)
# print(node1.val)
# print(node1.next)

# creating singly linked list

class SinglyLinkedlist:
    def __init__(self):
        self.head=None
        
    def append(self,val):
        new_node=Node(val)
        if self.head ==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
        
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
        
    def insert_at(self,val,position):
        new_node=Node(val)
        if position ==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current= self.head
            prev_node=None
            count=0
            while current is not None and count <position:
                prev_node=current
                current=current.next
                count+=1
                    
            prev_node.next=new_node
            new_node.next=current
        
    def delete(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next 
                return 
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                            
                    prev=temp
                    temp=temp.next 
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Node not found")

sll=SinglyLinkedlist()
sll.append(5)
sll.append(10)    
sll.append(15)
sll.append(20)
sll.traversal()
print()
sll.insert_at(25,2)
sll.traversal()
print()
sll.delete(10)
sll.traversal()
      