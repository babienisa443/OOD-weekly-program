print(" *** Min Max Avg ***")
inp = list(map(float, input("Enter 3 numbers : ").split()))
inp.sort()
print(f"min, mid, max ==> {inp[0]}, {inp[1]}, {inp[2]}")
sum = (inp[0]+inp[1]+inp[2])/3
print("Average ==> {:.2f}".format(sum))
