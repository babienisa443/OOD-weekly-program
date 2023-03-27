def permu(num,n):
    if n==0:
        print (num)
        return
    permu(num+'0',n-1)
    permu(num+'1',n-1)
        
n = int(input("Enter Number: "))
if n<0:
    print("Only Positive & Zero Number ! ! !")
permu('',n)
