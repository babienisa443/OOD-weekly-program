class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,tmp):
        self.items.append(tmp)
    
    def isEmpty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    
b=[e for e in input("Enter Input : ").split(",")]
s=Stack()
s2=Stack()
for i in b:
        if i[0]=='A':
            s.push(int(i[2:]))
            print("Add = "+i[2:])

        elif i[0]=='P':
            if s.isEmpty(): print("-1")
            else: print("Pop = "+str(s.pop()))

        
        elif i[0]=='D':
            
            if s.isEmpty():print("-1")
            else: 
                while not s.isEmpty():
                   
                  a=s.pop()
                  if a==int(i[2:]): 
                    print("Delete = "+str(a))
                  else:
                      s2.push(a)
                while not s2.isEmpty():
                          s.push(s2.pop())
        elif i[0]=='L':

            if s.isEmpty():print("-1")
            else: 
                while not s.isEmpty():
                  a=s.pop()
                  if a<int(i[3:]): 
                    print("Delete = "+str(a)+" Because "+str(a)+" is less than "+str(i[3:]))
                  else:
                      s2.push(a)
                while not s2.isEmpty():
                          s.push(s2.pop())
        elif i[0]=='M':
            if s.isEmpty():print("-1")
            else: 
                while not s.isEmpty():
                  a=s.pop()
                  if a>int(i[3:]): 
                    print("Delete = "+str(a)+" Because "+str(a)+" is more than "+str(i[3:]))
                  else:
                      s2.push(a)
                while not s2.isEmpty():
                          s.push(s2.pop()) 
ls=[]
while not s.isEmpty():ls.append(s.pop())                
print("Value in Stack = "+str(ls[::-1]))