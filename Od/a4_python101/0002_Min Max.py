import math
n = int(input())
Min = float('inf')
Max = float('-inf')
for i in range(n):

    inp = int(input())

    if inp < Min:
        Min = inp
    if inp > Max:
        Max = inp

print(Min)
print(Max)
