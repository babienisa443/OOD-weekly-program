class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
        self.prev=None
class doublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        
        self.head.next=self.tail
        self.tail.prev=self.head
    def __str__(self):
        s=''
        cur=self.head.next
        while cur!=self.tail:
            s+=str(cur.data)
            if cur.next.data!=None:
                s+=' '
            cur=cur.next
        return s
    def append(self,data):
        newNode=Node(data)
        newNode.next=self.tail
        self.tail.prev.next=newNode
        newNode.prev=self.tail.prev
        self.tail.prev=newNode
    def pop(self):
        popvalue=self.tail.prev.data     
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail
        
        return popvalue
    
    def isEmpty(self):
        return self.head.next.next == None
    
    def merge(self,ls):
        
        while not ls.isEmpty():
            
            self.append(ls.pop())        

L1,L2=doublyLinkedList(),doublyLinkedList()
l1,l2=input("Enter Input (L1,L2) : ").split()
l1=l1.split('->')
l2=l2.split('->')
for i in l1:
    L1.append(i)
print(f"L1    : {L1}")

for i in l2:
    L2.append(i)
print(f"L2    : {L2}")

L1.merge(L2)
print(f"Merge : {L1}")
    