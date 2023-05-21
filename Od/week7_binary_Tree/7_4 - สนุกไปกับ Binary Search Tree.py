class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        newNode=Node(data)
        if self.root ==None:
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
                
                
    def PrintTree(self,node,level):
        if node!=None:
            self.PrintTree(node.right,level+1)
            print("        "*level,node) 
            self.printTree(node.left,level+1)
            
    def inOrder(self,node):
        if node!=None:
            self.inOrder(node.left)    
            print(node,end=' ')
            self.inOrder(node.right)
            
    def preOrder(self,node):
        if node!=None:
            print(node,end=' ')
            self.preOrder(node.left)    
            self.preOrder(node.right)
    
    def postOrder(self,node):
        if node!=None:
            self.postOrder(node.left)    
            self.postOrder(node.right)
            print(node,end=' ')
            
    def breadth(self,node,q = []):
        if node!=None:
            print(node,end=' ')
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
            if len(q)!=0:
                self.breadth(q.pop(0),q)
            else:
                return
                
                

T=BST()
inp=[int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root=T.insert(i)
   
    
print("Preorder : ",end='')
T.preOrder(root)
print("\nInorder : ",end='')
T.inOrder(root)
print("\nPostorder : ",end='')
T.postOrder(root)
print("\nBreadth : ",end='')
T.breadth(root)