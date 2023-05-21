#palindrome
# def palindrome(n,i):
#     if i>0:
#         return n[i]+palindrome(n, i-1)
#     else:
#         return n[i]

# inp=input("Enter Number : ")
# if inp==palindrome(inp,len(inp)-1):
#     print(f"'{inp}' is palindrome")
# else:
#     print(f"'{inp}' is not palindrome")

#fibo

# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# inp=int(input("Enter Number : "))
# print(f"fibo({inp}) = {fibo(inp)}")

#2^(input)-1

# def permu(s,n):
#     if n==0:
#         print(s)
#         return
#     else:
#         permu(s+'0',n-1)
#         permu(s+'1',n-1)

# inp=int(input("Enter Number : "))
# if inp<0:
#     print("Only Positive & Zero Number ! ! !")
# permu(" ",inp)

#fac
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fac(n-1)


# inp=int(input("Enter Number : "))
# print(f"{inp}! = {fac(inp)}")

def is_palindrome(s, lower=0, upper=None):
    """
    Checks if a string is a palindrome while ignoring case.
    Args:
        s (str): The string to check.
        lower (int): The lower index of the substring to check.
        upper (int): The upper index of the substring to check.
    Returns:
        True if the string is a palindrome, False otherwise.
    """
    if upper is None:
        upper = len(s) - 1
    if lower >= upper:
        return True
    elif s[lower].lower() != s[upper].lower():
        return False
    else:
        return is_palindrome(s, lower+1, upper-1)
    
s=input("Enter :")
