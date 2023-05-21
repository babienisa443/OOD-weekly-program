def max(n):
    if len(n) == 1:
        return n[0]
    elif n[0] < n[1]:
        return max(n[1:])
    else:
        n.pop(1)
        return max(n)
inp=list(map(int,input('Enter input : ').split()))
print(f"Max : {str(max(inp))}")