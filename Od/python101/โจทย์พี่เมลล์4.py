inp = list(map(int, input().split()))
odd = []
even = []
for i in inp:
    e = i
    if e % 2 == 0:
        even.append(e)
    else:
        odd.append(e)
print(even, odd)
