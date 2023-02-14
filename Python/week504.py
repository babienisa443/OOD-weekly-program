class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous = None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
            
    def isEmpty(self):
        return self.head==None
    
    
    def insert(self, pos, item):
        a=Node(item)
       
        if self.isEmpty():
            self.head=a
            self.tail=a
            
        elif pos==0 or -1*pos>self.size():
            self.head.previous=a
            a.next=self.head
            self.head=a
              
        elif pos>self.size()-1: #ตั้งเเต่ตัวสุดท้ายถึงอนันต์
            self.tail.next=a
            a.previous=self.tail
            self.tail=a
        
        elif pos>0:
            t=self.head
            i = 0
            while i<pos-1:
                i+=1
                t=t.next
            a.next = t.next
            t.next.previous = a
            t.next = a
            a.previous = t
        else:
            p=self.tail
            i=1
            while i<-1*pos:
                i+=1
                p=p.previous
            a.previous=p.previous
            p.previous.next=a
            p.previous=a
            a.next=p
    
    
    def pop(self, pos):
       if pos<0 or pos>=self.size():
            return "Out of Range"
       else:
            i=0
            cur=self.head
            while i<pos:
                cur=cur.next
                i+=1
            if self.size()==1:
                self.head=None
                self.previous=None
            elif i==0:
                self.head = cur.next
                self.head.previous = None
            elif i==self.size()-1:
                self.tail = cur.previous
                self.tail.next = None
            else:
                cur.next.previous = cur.previous
                cur.previous.next = cur.next
            return "Success"        
                
    
    def size(self):
        h=self.head
        index=0
        while h !=None:
            index+=1
            h=h.next
        return index
    
l=linkedlist()
l.append("|")
cur=0
inp= input("Enter Input : ").split(',')
for i in inp:
     if i[0]=="I":
        l.insert(cur,i[2:])
        cur+=1
     elif i[0]=="L":
        if cur!=0:
            l.pop(cur)
            cur-=1
            l.insert(cur,"|")
     elif i[0]=="R":
        if cur!=l.size()-1:
            l.pop(cur)
            cur+=1
            l.insert(cur,"|")
     elif i[0]=="B":
        if cur!=0:
            cur-=1
            l.pop(cur)
     else:
        if cur!=l.size()-1:
            l.pop(cur+1)
print(l.__str__())
        
        
            
            