class Calculator:

    def __init__(self, data):
        self.data = data

    def __add__(self, calculator_obj):
        return self.data + calculator_obj.data

    def __sub__(self, calculator_obj):

        return self.data - calculator_obj.data

    def __mul__(self, calculator_obj):

        return self.data * calculator_obj.data

    def __truediv__(self, calculator_obj):

        return self.data / calculator_obj.data


x, y = input("Enter num1 num2 : ").split(",")

a, b = Calculator(int(x)), Calculator(int(y))

print(a+b, a-b, a*b, a/b, sep="\n")

