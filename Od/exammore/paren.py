class Stack:
    def __init__(self, data=None) -> None:
        if data is None:
            self.data = []
        else:
            self.data = data

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop(-1)

    def size(self):
        return len(self.data)

    def peek(self):
        if self.isEmpty():
            return 
        else:
            return self.data[-1]


def paren(data):
    paren = {')': '(', ']': '['}
    s = Stack()
    for i in data:

        if i in list(paren.values()):
            s.push(i)
        else:

            if paren[i] == s.peek():
                s.pop()
            

    if s.isEmpty():
        print(True)
    else:
        print(False)


inp = input("Enter input : ")
paren(inp)
