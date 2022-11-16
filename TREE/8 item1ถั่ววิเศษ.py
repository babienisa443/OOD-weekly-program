class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None 
    
    
    
    def insert(self,data:int):
        buffer=[]
        def _insert(data,curNode:Node or None):
            nonlocal buffer
       
            if data<curNode.data:
                buffer.append('L')
                if not curNode.left:
                    curNode.left=Node(data)
                else:
                    _insert(data,curNode.left)
            
            else:
                buffer.append('R')
                if not curNode.right:
                     curNode.right=Node(data)
                else:
                    _insert(data,curNode.right)
        
        if not self.root:
            self.root=Node(data)
        else:
            _insert(data,self.root)
        s=""
        for i in buffer:
            s+=i
        return f'{s}*'
    
t = BST()
inp = [int(i)for i in input("Enter Input : ").split()]
for i in inp:
    print(t.insert(i)) 