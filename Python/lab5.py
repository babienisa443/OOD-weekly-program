n=int(input("Enter Input : "))
for i in range(n+2):#n always have to more than i 
    for j in range(n-i+1):
        print(".",end="")
    for j in range(i+1):
        print("#",end="")
    for j in range(n+2):
        if j==0 or j==n+1 or i==0 or i==n+1 :
            print("+",end="")
        
        else:
            print("#",end="")
    print("")
    
 #below   
for i in range(n+2):
    for j in range(n+2):
        if j==0 or j==n+1 or i==0 or i==n+1 :
            print("#",end="")
        
        else:
            print("+",end="")
    for j in range(n-i+2):
        print("+",end="")
    for j in range(i):
        print(".",end="")
    print("")