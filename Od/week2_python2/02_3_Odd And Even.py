def Odd_Even(data, operation):
    ls = []

    for i in range(len(data)):

        if operation == 'Even':
            if i % 2 != 0:
                ls.append(data[i])

        else:
            if i % 2 == 0:
                ls.append(data[i])
    return ls


print("*** Odd Even ***")
t, data, operation = input("Enter Input : ").split(",")


if t == 'S':

    print(''.join(Odd_Even(data, operation)))
else:
    data = data.split()
    print(Odd_Even(data, operation))
