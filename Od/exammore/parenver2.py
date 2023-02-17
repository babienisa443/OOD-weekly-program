class Stack:
    def __init__(self, data=None) -> None:
        if data is None:
            self.data = []
        else:
            self.data = data

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.data[-1]
def paren(data):
    s=Stack()
    paren_check={')':'(',']':'['}
    for i in data:
        
        if i in list(paren_check.values()):
                s.push(i)
        else:
            if paren_check[i]==s.peek():
                s.pop()
    
    if s.isEmpty():
        print("Parentheses : Matched!!!")
    else:
        print("Parentheses : Unmatched!!!")            
inp = list(*input("Enter input : ").split())
paren(inp)



# dic[0] = key at index 0
# dic[key] = value at key
# dic.values() = list of values 
# dic.keys() = list of keys