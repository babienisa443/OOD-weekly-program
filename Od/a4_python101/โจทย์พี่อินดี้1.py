
def BanlowerStr(inp):
    ls = []
    for i in inp:
        if i.isupper():
            ls.append(i)

    return ls


inp = input()
B = BanlowerStr(inp)
print(''.join(B))
