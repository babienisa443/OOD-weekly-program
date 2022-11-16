class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
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
                         
    def printtree(self, node, level = 0):
        if node != None:
            self.printtree(node.right, level + 1)
            print('     ' * level, node)
            self.printtree(node.left, level + 1)
def postToPre(post_exp):
    s = []
    for i in range(len(post_exp)):
        if (post_exp[i]in"+-*/"):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i]) 
    ans = ""
    for i in s:
        ans += i
    return ans
def postToIn(post_exp):
    s = []
    for i in range(len(post_exp)):
        if (post_exp[i]in"+-*/"):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = '(' + op2 + post_exp[i] + op1 + ')'
            s.append(temp)
        else:
            s.append(post_exp[i])    
    ans = ""
    for i in s:
        ans += i
    return ans
class stack():
    def __init__(self) :
        self.e = []
    def push(self,data):
        self.e.append(data)
    def isEmpty(self):
        return len(self.e)==0
    def peek(self):
        if not self.isEmpty():
            return self.e[-1]
    def pop(self):
        if not self.isEmpty():
            return self.e.pop()
y = BST()
st = stack()
x = input('Enter Postfix : ')
for i in x:
    if i in '+-*/':
        r = st.pop()
        l = st.pop()
        st.push(Node(i,l,r))
    else :
        st.push(Node(i))
print("Tree :")
y.root = st.pop()
y.printtree(y.root)
print('--------------------------------------------------')
print("Infix :", postToIn(x))
print("Prefix :",postToPre(x))