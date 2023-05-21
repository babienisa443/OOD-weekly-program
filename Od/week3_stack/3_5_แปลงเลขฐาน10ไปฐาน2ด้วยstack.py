class Stack:

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0


def dec2bin(decnum):

    s = Stack()
    while decnum >= 2:
        x = decnum % 2
        s.push(x)
        decnum //= 2
    s.push(decnum)
    value=''
    while not s.isEmpty():
       value+=str(s.pop())
    return value


print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ", end='')

print(dec2bin(int(token)))
