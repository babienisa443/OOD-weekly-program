class Node(object):
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
        self.height=0
    def __str__(self):
        return str(self.data)
    
class AVL_Tree(object):
    def __init__(self):
        self.root=None
        
    def lotateleft(self,px):
        py=px.left
        px.left=py.right
        py.right=px
        return py
    def lotateright(self,px):
        py=px.right
        px.right=py.left
        py.left=px
        return py
    def height(self,h):
        if h is not None:
            h.height=max(self.height(h.left),self.height(h.height))+1
            return h.height
        else:
            return -1
    def insert(self,node,data):
        data=int(data)
        if not self.root:
            self.root=Node(data)
            return Node(data)
        else:
            if node !=None:
                if node.data>data:
                    node.left=self.insert(node.left,data)
                else:
                    node.right=self.insert(node.right,data)
            else:
                return Node(data)
    
            
            l=node.left.height if node.left is not None else -1
            r=node.right.height if node.right is not None else -1
            if abs(r-1)<1:
                if l>r:
                    cur=self.root
                    if node.left.data>data:
                        cur=self.lotateleft(node.left)
                    else:
                        node.left=self.lotateright(node.left)
                        node=self.lotateleft(node)
                        cur=node
                        
        
    