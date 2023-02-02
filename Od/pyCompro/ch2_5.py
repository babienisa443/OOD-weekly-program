print(" *** Number Fun !!! ***")
a, b = input("Enter a b : ").split()
print("a=", a, "\ttype =", type(a))
print("b=", b, "\ttype =", type(b))
a = int(a)
b = int(b)
n = a//b
m = a % b
n2 = b//a
m2 = b % a
print("a/b = {:.2f}".format((a/b)))
print("b/a = {:.3f}".format((b/a)))
print(f"a/b = {n} r {m}".format(n, m))
print(f"b/a = {n2} r {m2}".format(n2, m2))

# convert a to int
# convert b to int
# แสดงผล a/b ทศนิยม 2 ตำแหน่ง
# แสดงผล b/a ทศนิยม 3 ตำแหน่ง
# แสดงผลการหารแบบเหลือเศษของ a และ b
# แสดงผลการหารแบบเหลือเศษของ b และ a
