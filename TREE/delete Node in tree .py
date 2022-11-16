class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        cur=Node(val)
        
        if self.root is None:
                 self.root=cur
                 return self.root
                 
        else:
                  temp=self.root
                  while temp!=None:
                    if temp.data>=val  :
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
    def delete(self,r, data):
           
        if r == None :
            print('Error! Not Found DATA')
            return
        if r.data!=data:
            if r.data<=data:
                r.right = self.delete(r.right, data)
            elif r.data>data:
                r.left = self.delete(r.left, data)
        else:
            if r.right == None:
                r = r.left
                return r
            elif r.left == None:
                r = r.right
                return r
            else :
                temp = r.right
                while temp.left!=None :
                    temp = temp.left
                r.data = temp.data
                r.right = self.delete(r.right,temp.data)
               
        return r       
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in range (len(data)):
    t = data[i].split()
    if t[0]=='i':
        print('insert '+str(t[1]))
        tree.insert(int(t[1]))
        printTree90(tree.root)
    elif t[0]=='d':
        print('delete '+str(t[1]))
        tree.root = tree.delete(tree.root,int(t[1]))
        printTree90(tree.root)

