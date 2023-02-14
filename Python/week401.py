


class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.size()>0 else -1
    
    def enqueue(self,tmp):
        self.items.append(tmp)
    
    def dequeue(self):
        return self.items.pop(0) if self.size()>0 else -1
    
    
    
    
ls=[e for e in input("Enter Input : ").split(",")]
q=Queue()

for i in ls:
    if i[0]=='E': 
        
        print("Add "+i[2:]+" index is "+str(q.size()))
        q.enqueue(int(i[2:]))
    else: 
        x=q.dequeue()
        if x==-1:
            print(x)
        else:
            print("Pop "+str(x)+" size in queue is "+str(q.size()))
        
        
if q.isEmpty():
    print("Empty")
else:
    #("Number in Queue is : "+str(q.items),end='')
    print("Number in Queue is :  [",end="")
    for i in range(len(q.items)):
        print("'"+str(q.items[i])+"'",end="")
        if i != len(q.items)-1:
            print(", ",end="")
    print(']')
    
    
            