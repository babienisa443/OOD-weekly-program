def Trik(inp):
    ls = [True, False, False]
    for i in inp:
        if i == 'A':
            ls[0], ls[1] = ls[1], ls[0]
        elif i == 'B':
            ls[1], ls[2] = ls[2], ls[1]
        else:
            ls[0], ls[2] = ls[2], ls[0]
    return ls


inp = input()
result = Trik(inp)
print(result.index(True)+1)
