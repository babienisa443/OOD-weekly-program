class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __str__(self):
        if self.head.next==None:
            return "Empty"
        cur = self.head
        s=""
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        if self.size()== 0:
            return
    

    def append(self, data):
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def addHead(self, data):
        newNode = Node(data)
        cur = self.head
        newNode.next = cur.next
        cur.next = newNode

    def search(self, data):
        cur = self.head
        while cur.next != None:
            if cur.next.data == data:
                return 'Found'
            cur = cur.next
        return 'Not Found'

    def index(self, data):
        cur = self.head
        i = 0
        while cur.next != None:
            if cur.next.data == data:
                return i
            cur = cur.next
            i += 1
        return -1

    def size(self):
        size = 0
        cur = self.head
        while cur.next != None:
            size += 1
            cur = cur.next
        return size

    def pop(self, pos):
        if pos<0 or pos>=self.size():
            return 'Out of Range'
        # elif pos==0:
        #     self.head=self.head.next
        else:
            cur=self.head
            for i in range(pos):
                cur=cur.next
            cur.next=cur.next.next
        return 'Success'
       
            
            
            
            
            


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) 
              if k =="Success" 
              else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
