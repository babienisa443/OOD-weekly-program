class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class Likedlist:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.previous = self.head

    def __str__(self):  # return string แสดง ค่าใน linked list
        if self.isEmpty():
            return "Empty"
        else:
            s = ''
            cur = self.head.next
            while cur != self.tail:
                s += str(cur.data)
                if cur.next.data != None:
                    s += '->'
                cur = cur.next
            return s

    def str_reverse(self):  # return string แสดง ค่าใน linked list จากหลังมาหน้า
        if self.isEmpty():
            return "Empty"
        else:
            s = ''
            cur = self.tail.previous
            while cur.previous != None:
                s += str(cur.data)
                if cur.previous.data != None:
                    s += '->'
                cur = cur.previous
            return s

    def isEmpty(self):  # return list นั้นว่างหรือไม่
        return self.head.next.next == None

    def append(self, data):  # add node ที่มี data เป็น parameter ข้างท้าย linked list
        curNode = Node(data)

        curNode.next = self.tail
        self.tail.previous.next = curNode
        curNode.previous = self.tail.previous
        self.tail.previous = curNode
        self.size += 1

    def insert(self, index, data):  # insert data ใน index ที่กำหนด
        if (index > self.size-1 or index < 0) and index != 0:
            print("Data cannot be added")
            return
        else:

            newNode = Node(data)
            cur = self.head

            for i in range(index):
                cur = cur.next
            newNode.previous = cur
            newNode.next = cur.next
            cur.next.previous = newNode
            cur.next = newNode
            self.size += 1
            print(f'index = {index} and data = {data}')
            return

    def add_before(self, data):
        newNode=Node(data)
        cur=self.head
        newNode.next=cur.next
        newNode.previous=cur
        cur.next.previous=newNode
        cur.next=newNode
        

    def remove(self, data):  # remove & return node ที่มี data
        cur = self.head
        n = 0
        while n < self.size and cur.data != data:
            cur = cur.next
            n += 1
        if n > self.size or self.size == 0:
            print('Not Found!')
            return
        else:
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            print(f'removed : {data} from index : {n-1}')
            return


inp = input("Enter Input : ").split(',')
lk = Likedlist()
for i in inp:
    i = i.strip()
    inp1 = i.split()
    if inp1[0] == 'I':
        operation = inp1[1].split(':')
        lk.insert(int(operation[0]), operation[1])
    elif inp1[0] == 'Ab':
        lk.add_before(inp1[1])
    elif inp1[0] == 'A':
        lk.append(inp1[1])
    elif inp1[0] == 'R':
        lk.remove(inp1[1])
    print(f'linked list : {lk}')
    print(f'reverse : {lk.str_reverse()}')


