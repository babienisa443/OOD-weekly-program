class StackCalc:
    def __init__(self):
        self.stack = []

    def run(self, args):
        new_args = args.split()
        for arg in new_args:
            if arg in ['+', '-', '*', '/', 'DUP', 'POP', 'PSH']:
                if arg == '+':
                    self.stack.append(self.stack.pop()+self.stack.pop())
                elif arg == '-':
                    self.stack.append(self.stack.pop()-self.stack.pop())
                elif arg == '*':
                    self.stack.append(self.stack.pop()*self.stack.pop())
                elif arg == '/':
                    self.stack.append(self.stack.pop()//self.stack.pop())
                elif arg == 'DUP':
                    self.stack.append(self.stack[-1])
                elif arg == 'POP':
                    self.stack.pop()
            elif (arg >= 'a' and arg <= 'z') or (arg >= 'A' and arg <= 'Z'):
                self.stack.append(f"Invalid instruction: {arg}")
                return
            else:
                self.stack.append(int(arg))

    def getValue(self):
        if len(self.stack) == 0:
            return 0
        else:
            return self.stack[-1]


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
