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
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.value == item:
                return 'Found'
            cur = cur.next
        return 'Not Found'

    def index(self, item):
        i = 0
        cur = self.head
        while cur != None:
            if cur.value == item:
                return i
            cur = cur.next
            i += 1
        return -1

    def size(self):
        size = 0
        cur = self.head
        while cur != None:
            size += 1
            cur = cur.next
        return size

    def pop(self, pos):
        if pos >= self.size() or pos<0: 
            return 'Out of range'
        
        elif pos == 0:
            self.head = self.head.next
        elif pos == self.size()-1:
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None
        else:
            cur = self.head
            i = 0
            while i < pos-1:
                i += 1
                cur = cur.next
            cur.next = cur.next.next
        return 'Success'


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
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
