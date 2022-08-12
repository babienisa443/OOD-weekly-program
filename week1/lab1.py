print("*** Rabbit & Turtle ***")
d,Vr,Vt,Vf=input("Enter Input : ").split()
t=int(d)/(int(Vt)-int(Vr))
S=int(Vf)*t
print("{:.2f}".format(float(S)))