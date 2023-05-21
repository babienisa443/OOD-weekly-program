print(" *** integer summation from 1 to n ***")
inp = int(input("Enter an integer(n) : "))
i = 1
sum = 0
ls = []
while i <= inp:
    ls.append(str(i))
    sum += i
    i += 1

print("Summation =>", '+'.join(ls), end=' = ')
print(sum)
