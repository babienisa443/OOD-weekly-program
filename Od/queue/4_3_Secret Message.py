class Queue:
    def __init__(self, data=None) -> None:
        if data is None:
            self.data = []
        else:
            self.data = data

    def __str__(self) -> str:
        return str(self.data)

    def isEmpty(self):
        if self.data == []:
            return True
        else:
            return False

    def size(self):
        return len(self.data)

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


def encodemsg(q1, q2):
    q2_copy = Queue(q2.data.copy())
    for i in range(q1.size()):
        char = q1.dequeue()
        number = q2_copy.dequeue()

        if char >= 'a' and char <= 'z':
            char = chr(ord('a') + (ord(char)-ord('a')+number) % 26)
        elif char >= 'A' and char <= 'Z':
            char = chr(ord('A') + (ord(char)-ord('A')+number) % 26)

        q1.enqueue(char)
        q2_copy.enqueue(number)
    print(f'Encode message is :  {q1}')


def decodemsg(q1, q2):
    q2_copy = Queue(q2.data.copy())
    for i in range(q1.size()):
        char = q1.dequeue()
        number = q2_copy.dequeue()

        if char >= 'a' and char <= 'z':
            char = chr(ord('a') + (ord(char)-ord('a')+(26-number)) % 26)
        elif char >= 'A' and char <= 'Z':
            char = chr(ord('A') + (ord(char)-ord('A')+(26-number)) % 26)

        q1.enqueue(char)
        q2_copy.enqueue(number)

    print(f'Decode message is :  {q1}')


msg, secret = input("Enter String and Code : ").split(',')
msg = [*msg.replace(' ', '')]
secret = list(map(int, secret))
q1 = Queue(msg)
q2 = Queue(secret)
encodemsg(q1, q2)
decodemsg(q1, q2)
