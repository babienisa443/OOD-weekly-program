print(" *** Factorial ***")
inp = int(input("Enter an integer(n) : "))
i = 1
sum = 1
ls = []
while i <= inp:
    ls.append(str(i))
    sum *= i
    i += 1

print(f"Fac({inp}) =>", '*'.join(ls), end=' = ')
print(sum)
