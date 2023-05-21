def palindrome(t,i):

    if i>0:                     
      return t[i]+palindrome(t,i-1)
       
    else:
        return t[i]  
        
inp=input("Enter Input : ")
inp1=inp.split()
inp1=''.join(inp1)
ls=[]
for i in inp1:
    if i>='A'and i<='Z' or i>='a' and i<='z':
        ls.append(i)
ls=''.join(ls)
if ls.lower()==palindrome(ls.lower(),len(ls)-1):
    
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")