inp = input()
ls = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
sum = 0
for i in inp:
    if i in ls:
        sum += 1
print(sum)
