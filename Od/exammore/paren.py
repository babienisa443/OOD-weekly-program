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
        return self.data.pop()

    def size(self):
        return len(self.data)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.data[-1]


def paren(data):
    paren = {')': '('}
    s = Stack()
    for i in data:
        if i not in paren.values() and i not in paren.keys():
            continue
        if i == paren.values():
            s.push(i)
        else:
            p = s.peek()
            if paren == p:
                s.pop()
            
    if s.isEmpty():
            print(True)
    else:
        print(False)

inp = input("Enter input : ")
paren(inp)
