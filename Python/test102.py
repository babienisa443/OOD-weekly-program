class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def peek(self):
        return self.items[-1]
n=[e for e in input("Enter Input : ").split(',') ]
s=Stack()
s2=Stack()
for i in n:
    if i[0]=='A':
        s.push(int(i[2:]))
        print("Add = ",i[2:])
    elif i[0]=='P':
        if s.isEmpty():print("-1")
        else:
            print("Pop = "+str(s.pop()))
    elif i[0]=='D':
        if s.isEmpty():print("-1")
        else:
            while not s.isEmpty(): 
                k=s.pop()
                if k==(int(i[2:])):
                    print("Delete = "+str(k))
                else:
                    s2.push(k)
                    
            while not s2.isEmpty():
                 s.push(s2.pop())
    elif i[0]=='L':
        if s.isEmpty():print("-1")
        else:
            while not s.isEmpty():
                k=s.pop()
                if k<int(i[3:]):
                    print("Delete = "+str(k)+" Because "+str(k)+" less than "+str(i[3:]))
                else:
                    s2.push(k)
            while not s2.isEmpty():
                s.push(s2.pop())
    elif i[0]=='M':
        if s.isEmpty():print("-1")
        else:
            while not s.isEmpty():
                k=s.pop()
                if k>int(i[3:]):
                    print("Delete = "+str(k)+" Because "+str(k)+" is more than "+str(i[3:]))
                else:
                    s2.push(k)
            while not s2.isEmpty():
                s.push(s2.pop())
ls=[] 
while not s.isEmpty():ls.append(s.pop())                     
print("Value in Stack = "+str(ls[::-1]))        
        
                
                
                

        