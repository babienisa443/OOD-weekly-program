def Min(x):
    if len(x)==1:
        return x[0]
    else:
        return min(x[0],Min(x[1:]))
    
inp=[int(i) for i in input("Enter input : ").split(" ")]
print(f"Min : {Min(inp)}")