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
                    if data<=temp.data  :
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
              
                
                    
                  

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)