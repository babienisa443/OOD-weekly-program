class LinkedQueue :
    class Node :
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0

    def __str__(self):
        strList = ""
        temp = self.head
        while temp :
            if temp == None :
                strList += ""
                break
            elif temp.next == None :
                strList += str(temp.data)
            else :
                strList += (str(temp.data)+" ")
            temp = temp.next
        return strList

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self) :
        if self.isEmpty():
            print("Queue is empty")
        else :
            return self.head

    def dequeue(self):
        if self.isEmpty() :
            print("Queue is empty")
            return 
        elif self.size == 1 :
            answer = self.head
            self.head = None
            self.tail = None
            self.size -= 1
        else :
            answer = self.head
            self.head = self.head.next
            self.size -= 1
        return answer.data

    def enqueue(self,data):
        temp = self.head
        newNode = self.Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        else :
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def enqueue_sort(self,data):
        temp = self.head
        newNode = self.Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return
        if temp.data > data :
            newNode.next = temp
            self.head = newNode
            self.size += 1
            return
        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        self.size += 1

def getDigit(n,d):
    if n < 0 :
        n *= -1
    i = d 
    while i > 1 :
        n //= 10
        i-=1
    return n % 10

def getMaxDigit(n):
    if n < 0 :
        n *= -1
    i = 0
    while n > 0 :
        n //= 10
        i += 1
    return i

def radixSort(l):
    listMax = []
    for i in range(len(l)):
        listMax.append(getMaxDigit(l[i]))
    maxBits = max(listMax)
    q = LinkedQueue()
    for i in range(len(l)):
        q.enqueue(int(l[i]))
    qq = [LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),
          LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue()]
    qqn = [LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),
          LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue(),LinkedQueue()]
    times = 0
    for i in range(1,maxBits+1):
        while not q.isEmpty() :
            num = q.dequeue()
            indexDigit = int(getDigit(num,i))
            if num < 0 :
                qqn[indexDigit].enqueue(int(num))
            else :
                qq[indexDigit].enqueue(int(num))
        print("------------------------------------------------------------")
        print("Round : " + str(i))
        for j in range(10):
            print(str(j) + " : ",end = "")
            if qqn[j].isEmpty():
                print("",end="")
            else :
                print(qqn[j].__str__(),end = " ")
            print(qq[j].__str__())
        for k in range(len(qqn)-1,-1,-1):
            while not qqn[k].isEmpty():
                q.enqueue(int(qqn[k].dequeue()))
        for k in range(10):
            while not qq[k].isEmpty():
                q.enqueue(int(qq[k].dequeue()))
        times += 1
    print("------------------------------------------------------------")
    print(str(times) + " Time(s)")    
    print("Before Radix Sort : ",end="")
    for i in range(len(l)-1):
        print(l[i],end=" -> ")
    print((l[-1]))
    print("After  Radix Sort : ",end="")
    for i in range(q.size-1):
        print(str(q.dequeue()),end=" -> ")
    print(q.dequeue())
inp = list(input("Enter Input : ").split(" "))
inp = [int(j) for j in inp]
radixSort(inp)
