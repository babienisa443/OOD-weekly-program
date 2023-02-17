class Queue:
    def __init__(self, keys=None) -> None:
        if keys is None:
            self.keys = []
        else:
            self.keys = keys

    def __str__(self) -> str:
        return ', '.join(self.keys)

    def enqueue(self, keys):
        self.keys.append(keys)

    def dequeue(self):
        return self.keys.pop(0)

    def isEmpty(self):
        return len(self.keys) == 0




inp = input("Enter Input : ").split(",")
my_queue = Queue()
your_queue = Queue()

for i in range(len(inp)):
    my, your = inp[i].split(" ")
    my_queue.enqueue(str(my))
    your_queue.enqueue(str(your))

print("My   Queue =", my_queue)
print("Your Queue =", your_queue)

activity = {'0': 'Eat', '1': 'Game', '2': 'Learn', '3': 'Movie'}
location = {'0': 'Res.', '1': 'ClassR.', '2': 'SuperM.', '3': 'Home'}

count = 0
my_text = []
your_text = []
while not my_queue.isEmpty():
    my_q, your_q = my_queue.dequeue(), your_queue.dequeue()
    my_text.append(f'{activity[my_q[0]]}:{location[my_q[2]]}')
    your_text.append(f'{activity[your_q[0]]}:{location[your_q[2]]}')

    if my_q[0] == your_q[0] and my_q[2] != your_q[2]:
        count += 1
    elif my_q[0] != your_q[0] and my_q[2] == your_q[2]:
        count += 2
    elif my_q[0] == your_q[0] and my_q[2] == your_q[2]:
        count += 4
    else:
        count -= 5

print("My   Activity:Location =", ', '.join(my_text))
print("Your Activity:Location =", ', '.join(your_text))

if count >= 7:
    print(f"Yes! You're my love! : Score is {count}.")
elif count < 7 and count > 0:
    print(f"Umm.. It's complicated relationship! : Score is {count}.")
else:
    print(f"No! We're just friends. : Score is {count}.")
