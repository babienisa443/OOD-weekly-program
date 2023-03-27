inp = int(input())
sum = 0

for i in range(1, inp):
    if inp % i == 0:
        sum += i
if sum == inp:
    print(sum, 'Is perfect number')
else:
    print(sum, 'Is not perfect number')
