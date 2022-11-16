
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
    
class BST:
        def __init__(self):
            self.root=None
            
        def insert(self,data):
              cur=Node(data)
              if self.root is None:
                 self.root=cur
                 return self.root
                 
              else:
                  temp=self.root
                  while temp!=None:
                    if temp.data>=data  :
                        if temp.left == None:
                            temp.left = cur
                            return self.root
                        else:
                            temp=temp.left
                            
                    else:
                        if temp.right == None:
                            temp.right = cur
                            return self.root
                        else:temp=temp.right
                         
                         
        def printTree(self, node, level = 0):
                if node != None:
                    self.printTree(node.right, level + 1)
                    print('     ' * level, node)
                    self.printTree(node.left, level + 1)
        def FindMin(self):
            r=self.root
            while r is not None:
               if r.left is not None:
                    r=r.left
               else:
                    return r.data
        
        def FindMax(self):
            r=self.root
            while r is not None:
                if r.right is not None:
                    r=r.right
                else:
                    return r.data
            
                      
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.FindMin())
print("Max :",T.FindMax())
              
                
            
                
                    
                  
