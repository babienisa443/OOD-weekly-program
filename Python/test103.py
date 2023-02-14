class Stack:
    def __init__(self):
        self.items=[]
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
n = input('Enter Input : ').split()
n.reverse()
S = Stack()
b=0
for i in n:
    
    if S.size()<2:
        S.push(i)
    else:
        if i==S.peek() and S.peek()==S.items[-2]:
            S.pop()
            S.pop()
            b+=1
        else:
            S.push(i)

print(S.size())
if S.size()==0:
    print("Empty")
else:
    for i in S.items:
        print(i,end='')
    print()
if b>=2:
    print("Combo : "+str(b)," ! ! !")
