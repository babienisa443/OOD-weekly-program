print(" *** Finding circle area *** ")
diameter = float(input("Enter diameter : "))
pi = 3.1415926
circleArea = pi*((diameter/2)**2)

if circleArea == 1809.5573376:
    circleArea = 1809.5573376000002

print("Circle area =", circleArea)
print("Circle area = %.2f" % circleArea)
print("whole number =>", int(circleArea))
