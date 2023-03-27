import math
a, b = map(float, (input().split()))
ans = math.sqrt(a**2+b**2)
print("{:.6f}".format(ans))
