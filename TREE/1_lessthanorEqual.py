class Node:
    def __init__(self,data):
        self.data = data
        self.right=None
        self.left=None
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
                else:
                    if cur.right is None:
                        cur.right=new
                        return self.root
                    else:
                        cur=cur.right
    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("     "*level,node)
            self.printTree(node.left,level+1)
    def countK(self,node,k,sum=0):
        
        if node is not None:
            if node.data<=k:
                sum=1
            sum+=self.countK(node.left,k)
            sum+=self.countK(node.right,k)
        return sum

T = BST()
inp,k = input('Enter Input : ').split("/")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.countK(root,int(k)))


# 10 4 20 1 5/4
#0 -50 50 25 13 -13 28 -38 75 -75 62 -62 100 -100/-101