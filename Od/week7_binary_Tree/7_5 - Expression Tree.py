class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def printTree(node, level=0):
    if node != None:
        printTree(node.right, level+1)
        print("     "*level, node)
        printTree(node.left, level+1)

def tree(inp):
    q = []
    for i in inp:
        if i not in {'+', '-', '*','/'}:
            q.append(i)
        else:
            n = Node(i)
            if type(q[-1]) == str:
                n.right = Node(q.pop(-1))
            else:
                n.right = q.pop(-1)
            if type(q[-1]) == str:
                n.left = Node(q.pop(-1))
            else:
                n.left = q.pop(-1)

            q.append(n)
    return q.pop(0)

def infix(inp, n=[]):
    for i in inp:
        if i.isalpha():
            n.append(i)
        else:
            operator2 = n.pop()
            operator1 = n.pop()
            infix = f"({operator1}{i}{operator2})"
            n.append(infix)
    print(n[0])

def prefix(node):
    if node != None:
        print(node, end='')
        prefix(node.left)
        prefix(node.right)

inp = input("Enter Postfix : ")
print("Tree :")
printTree(tree(inp))
print('--------------------------------------------------')
print("Infix : ", end='')
infix(inp)
print("Prefix : ", end='')
prefix(tree(inp))
