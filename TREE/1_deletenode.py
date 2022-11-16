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
        new=Node(data)
        if not self.root:
            self.root=new
            return self.root
        else:
            cur=self.root
            while True:
                if cur.data>data:
                    if cur.left is None:
                        cur.left=new
                        return self.root
                    else:
                        cur=cur.left
                elif cur.data<data:
                    if cur.right is None:
                        cur.right=new
                        return self.root
                    else:
                        cur=cur.right
    
    def FindMin(self,root):
        r=root
        while r.left is not None:
                r=r.left
        return r
    def FindMax(self,root):
        r=root
        while r is not None:
                r=r.right
        return r
    
    def delete(self,root,data):
       
        if root is None:
            return root
        
        if root.data>data:
            root.left=self.delete(root.left,data)
        if root.data<data:
            root.right=self.delete(root.right,data)
            
        if data==root.data:
            
            if root.left is None:
                temp=root.left
                root=None
                return temp
            elif root.right is None:
                temp=root.right
                root=None
                return temp
            else:
                finishValue=self.FindMin(root.right)
                
                root.data = finishValue.data
                
                root.right=self.delete(root.right,finishValue.data)
        return root
                
def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)
        
tree = BST()
data = input("Enter Input : ").split(",")
for i in range (len(data)):
    t = data[i].split()
    if t[0]=='i':
        print('insert '+str(t[1]))
        tree.insert(int(t[1]))
        printTree(tree.root)
    elif t[0]=='d':
        print('delete '+str(t[1]))
        tree.root = tree.delete(tree.root,int(t[1]))
        printTree(tree.root)
       
        
       
                 
            
        
            
            
            
        
        
   
                
                
            
                        
        
                
        
        