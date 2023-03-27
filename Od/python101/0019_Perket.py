def Perget(sour, bitter):
    sum_sour = 1
    sum_bitter = 0
    for i in sour:
        sum_sour *= i
    for i in bitter:
        sum_bitter += i
    return abs(sum_sour-sum_bitter)




inp = int(input())

sour = []
bitter = []
for i in range(inp):
    S, B = map(int, input().split())
    sour.append(S)
    bitter.append(B)
    

print(Perget(sour, bitter))
