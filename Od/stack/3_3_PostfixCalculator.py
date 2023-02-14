class Stack():

    def __init__(self, ls=None):
        if ls is None:
            self.ls = []
        else:
            self.ls = ls

    def __str__(self):
        return ' '.join(self.ls)

    def push(self, i):
        self.ls.append(i)

    def pop(self):
        if self.ls == []:
            return
        else:
            return self.ls.pop(-1)

    def isEmpty(self):
        return len(self.ls) == 0

    def size(self):
        if self.size() == []:
            return True
        else:
            return len(self.ls)


def postFixeval(st):

    s = Stack()
    for i in st:
        if i in ['+', '-', '*', '/']:

            if i == '+':
                s.push(float(s.pop())+float(s.pop()))

            elif i == '-':
                a = s.pop()
                b = s.pop()
                s.push(float(b)-float(a))

            elif i == '*':
                s.push(float(s.pop())*float(s.pop()))

            elif i == '/':
                fac = s.pop()
                div = s.pop()
                s.push(float(div)/float(fac))

        else:
            s.push(str(i))

    return s.pop()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ", '{:.2f}'.format(postFixeval(token)))
