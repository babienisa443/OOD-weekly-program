class Stack:
    def __init__(self,ls=[]):
        self.items = ls
    
    def push(self,i):
        self.items.append(i)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    
def postFixeval(st):
     s = Stack()
     for i in st:
         if i=='+':s.push(s.pop()+s.pop())
         elif i=='-':s.push(-1*s.pop()+s.pop())
         elif i=='*':s.push(s.pop()*s.pop())
         elif i=='/':
             a=s.pop()
             b=s.pop()
             s.push(b/a)
         else:
             s.push(float(i))
     return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print(postFixeval(token))