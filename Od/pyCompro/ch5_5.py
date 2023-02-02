print(" *** even integer summation from 1 to n ***")
inp = int(input("Enter an integer(n) : "))
i = 2
sum = 0
ls = []
while i <= inp:
    if i % 2 == 0:
        ls.append(str(i))
        sum += i
        i += 2

print("Summation =>", '+'.join(ls), end=' = ')
print(sum)
