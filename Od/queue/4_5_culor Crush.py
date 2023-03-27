class Queue:
    def __init__(self, data=None) -> None:
        if data == None:
            self.data = []
        else:
            self.data = data

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0

    def rev(self, input):
        for i in range(len(self.data)):
            if self.data[i] == input:
                v = self.data.pop(i)
                self.data.insert(0, v)


q = Queue([1, 2, 3, 4, 5])
q.rev(5)
print(q.data)
