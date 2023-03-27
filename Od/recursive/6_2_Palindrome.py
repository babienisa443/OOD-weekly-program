def palindrome(t,i):

    if i>0:                     
      return t[i]+palindrome(t,i-1)
       
    else:
        return t[i]  
        
inp=input("Enter Input : ")
if inp==palindrome(inp,len(inp)-1):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")