def hbd(age):
    for base in range(2, age):
        if (age-20) % base == 0:
            return "saimai is just {} in base {}!".format(21, base)
        if (age-21) % base == 0:
            return "saimai is just {} in base {}!".format(20, base)
    return "No solution found"

year = input("Enter year : ")
print(hbd(int(year)))
