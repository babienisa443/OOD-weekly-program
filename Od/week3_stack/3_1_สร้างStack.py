class Stack:
    def __init__(self, data=[]):
        if data == []:
            self.data = []
        else:
            self.data = data

    def __str__(self) -> str:
        
        return ''.join(self.data)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop(-1)

    def isEmpty(self):
        if self.data == []:
            return True
        else:
            return False

    def size(self):

        return len(self.data)


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(), "Data in stack : ", s.data)

while not s.isEmpty():

    s.pop()

print(s.size(), "Data in stack : ", s.data)
