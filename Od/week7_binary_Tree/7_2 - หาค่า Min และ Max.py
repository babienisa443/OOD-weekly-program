class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode=Node(data)
        
        if self.root is None:
            self.root=newNode
            return self.root
        cur=self.root
        while True:
            if cur.data >=data:
                if cur.left==None:
                    cur.left=newNode
                    return self.root
                else:
                    cur=cur.left
            else:
                if cur.right==None:
                    cur.right=newNode
                    return self.root
                else:
                    cur=cur.right
    def Min(self):
        if self.root==None:
            return
        cur=self.root
        while True:
            if cur.left!=None:
                cur=cur.left
            else:
                return cur
                
    def Max(self):
        if self.root==None:
            return
        cur=self.root
        while True:
            if cur.right!=None:
                cur=cur.right
            else:
                return cur
            
            
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
print('--------------------------------------------------')
print(f"Min : {T.Min()}")
print(f"Max : {T.Max()}")

