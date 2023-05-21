class Queue:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def __str__(self) -> str:
        return str(self.data)

    def enqueue(self, data):
        return self.data.append(data)

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            return self.data.pop(0)

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


inp = [*input("Enter people : ")]
q_main = Queue(inp)
q1 = Queue()
q2 = Queue()
count_clk = 0
clock = 1
clock2 = 1

while not q_main.isEmpty():
    count_clk += 1
    if not q1.isEmpty():
        clock += 1
    if not q2.isEmpty():
        clock2 += 1

    if q1.size() < 5:
        q1.enqueue(q_main.dequeue())
    else:
        q2.enqueue(q_main.dequeue())
    print(f"{count_clk} {q_main} {q1} {q2}")

    if clock % 3 == 0:
        q1.dequeue()
        clock = 0
    if clock2 % 2 == 0:
        q2.dequeue()
        clock2 = 0
