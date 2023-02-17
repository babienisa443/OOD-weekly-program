class Stack:
    def __init__(self, data=None) -> None:
        if data is None:
            self.data = []
        else:
            self.data = data

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            return 
        else:
            return self.data[-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0


inp = input("Enter input : ").split(',')

s = Stack()


for i in inp:
    
    a=i.split()
    
    if a[0]=='A':
        s.push(int(a[1]))
     
    else:
       count=0
       temps= Stack(s.data.copy())
       height=temps.pop()
       count+=1
       while not temps.isEmpty():
            if temps.peek()>height:
               count+=1
               height=temps.pop()
            elif temps.peek()<=height:
               temps.pop()
            else:
               pass
       print(count)