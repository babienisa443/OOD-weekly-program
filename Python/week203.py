def newRange(n):
    s=0.0
    l=[s]
    
    while s<float(n):
        s+=1
        l.append(s)
    return l
def newRange(n,a):
    s=float(n)
    l=[s]
    
    while s<float(a):
        s+=1
        l.append(s)
    return l
def newRange(n,a,b):
    s=float(n)
    l=[s]
    
    while s<float(a):
        s+=1
        l.append(s)
    return l
n,a=input("Enter Input : ").split()

print(newRange(n))
    

