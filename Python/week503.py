class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)+''
        while cur.next != None:
            s += str(cur.next.value)+""
            cur = cur.next
        return s
    def isEmpty(self):
        return self.head==None
    def append(self,data):
        a=Node(data)
        if self.head is None:
            self.head=a
        else:
            t=self.head
            while t.next !=None:
                t=t.next
            t.next=a
    def size(self):
        h=self.head
        s=0
        while h !=None:
            s+=1
            h=h.next
        return s

a=LinkedList()
for i in input("Enter Input : ").split():
    a.append(i)

t = a.head
combo=0
i=0
while a.size()>2 and t.next.next !=None:
        if i==0 and t.value==t.next.value and t.value==t.next.next.value:
            if a.size()==3:
                a.head=None
                t=a.head
                combo+=1
            else:
                a.head=t.next.next.next
                t=a.head
                combo+=1
        elif t.next.value==t.next.next.value and t.next.value==t.next.next.next.value:
            combo+=1
            t.next=t.next.next.next.next
            i=0
            t=a.head
        else:
            t=t.next
            i+=1
        
print(a.size())
if a.size()>0:
    print(a.__str__()[::-1])
else:
    print("Empty")
if combo>1:
    print("Combo : "+str(combo)+" ! ! !")

                