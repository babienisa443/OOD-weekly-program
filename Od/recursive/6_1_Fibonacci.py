def fibonacci(n):
    if n <=1:
        return n
    return  fibonacci(n-1) + fibonacci(n-2)
inp=int(input("Enter Number : "))
print(f"fibo({inp}) = {fibonacci(inp)}")