class Stack:
    def __init__(self, list=None) -> None:
        if list is None:
            self.list = []
        else:
            self.list = list

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, list):
        self.list.append(list)

    def pop(self):
        return self.list.pop(-1)

    def size(self):
        return len(self.list)

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[-1]


def infix2postfix(exp):
    s = Stack()
    string = ''
    dicts = {'+': 1, '-': 1, '*': 2, '/': 2}
    for i in exp:
        if i in list(dicts.keys()):
            if s.isEmpty() or s.peek() == '(' or dicts[i] > dicts[s.peek()]:
                s.push(i)
            else:
                string += str(s.pop())
                s.push(i)
        elif i=='(':
            s.push(i)
        elif i==')':
            while not s.peek()=='(':
                string+=str(s.pop())
            s.pop()
        else:
            string += i

    while not s.isEmpty():
        a = s.pop()
        string += str(a)
    return string


print(" ***Infix to Postfix***")
token = input("enter infix expression : ")
print("PostFix:")
print(infix2postfix(token))
