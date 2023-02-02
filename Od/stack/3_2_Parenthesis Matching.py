class Stack:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def __str__(self) -> str:
        return ''.join(self.data)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def peek(self):
        if self.isEmpty():
            return None
        return self.data[-1]


def par_check(inp):
    pa_dict = {')': '(', '}': '{', ']': '['}
    stk = Stack()
    for i in inp:
        if i not in pa_dict.values() and i not in pa_dict.keys():
            continue

        if i in pa_dict.values():
            stk.push(i)

        else:
            pop_value = stk.peek()
            if pa_dict[i] == pop_value:
                stk.pop()

            else:
                if not stk.isEmpty():
                    print(f"{inp} Unmatch open-close")
                else:
                    print(f"{inp} close paren excess")
                return

    if not stk.isEmpty():
        print(f"{inp} open paren excess   {stk.size()} : {stk}")
        return

    else:
        print(f"{inp} MATCH")
        return


inp = input("Enter expresion : ")
par_check(inp)
