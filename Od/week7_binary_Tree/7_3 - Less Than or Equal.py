class Node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.data)
    
class bst:
    
    def __init__(self):
        self.root=None
    
    
    def insert(self,data):
        newNode=Node(data)
        if self.root is None:
            self.root=newNode
            return self.root
        cur=self.root
        while True:
            if cur.data>newNode.data:
                if cur.left!=None:
                    cur=cur.left
                else:
                    cur.left=newNode
                    return self.root
            else:
                if cur.right!=None:
                    cur=cur.right
                else:
                    cur.right=newNode
                    return self.root    
    def count(self,node,k):
        temp=0
        if node!=None:
           if node.data<=k:
               temp=1
           temp+=self.count(node.left,k)
           temp+=self.count(node.right,k)
        return temp
    
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node)
            self.printTree(node.left,level+1)
            
T=bst()
inp=input("Enter Input : ").split('/')
ls = [int(n) for n in inp[0].split()]
k=int(inp[1])
for i in ls:
    root=T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(T.count(root,k))
