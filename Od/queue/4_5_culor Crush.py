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


inp = input("Enter Input (Normal, Mirror) : ").split(" ")
q=Queue()


