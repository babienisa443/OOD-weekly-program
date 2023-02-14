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
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        ap = Node(item)
        if self.head is None:
            self.head = ap
        else:
            t=self.head 
            while t.next != None:
               
                t=t.next
            t.next=ap

    def addHead(self, item):
        n= Node(item)
        if self.isEmpty():
            self.head=n
        else:
            n.next=self.head
            self.head=n
            
            
    def search(self, item):
        h=self.head
        while h is not None:
            if h.value==item:
                return "Found"
            else:h=h.next
        return "Not Found"

    def index(self, item):
        h=self.head
        i=0
        while h is not None:
            if h.value==item:
                return i
            else:
                i+=1
                h=h.next
        return -1
    def size(self):
        h=self.head
        s=0
        while h is not None:
            s+=1
            h=h.next
        return s
    def pop(self, pos):
        
        if pos>self.size() or pos<0 or self.size()<=0:return "Out of Range"
        elif pos==0:
            h.head=None
            return "Success"
        else:
            h=self.head
            for i in range(pos-1): 
                h=h.next     
            h.next=h.next.next
            return "Success"
            
                

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)