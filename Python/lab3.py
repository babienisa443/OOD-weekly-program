print("*** Reading E-Book ***")
t,h=input("Text , Highlight : ").split(",")
for i in t:
    if i==h:
        print("[%c]"%(h),end="")
    else:
        print(i,end="")