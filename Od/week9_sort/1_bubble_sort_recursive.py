def bbsort(l,i=0,j=0):
    if i==len(l):return l
    if j==len(l)-i-1:return bbsort(l,i+1)
    if l[j] > l[j+1]:l[j], l[j+1] = l[j+1], l[j]
    return bbsort(l,i,j+1)

print(bbsort([int(i) for i in input("Enter Input : ").split()]))