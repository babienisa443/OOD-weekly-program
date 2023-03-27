inp = int(input())

if inp == 1:
    print(inp, 'Is not prime number')
elif inp <= 0:
    print('Input Error')
elif inp > 1:
    for i in range(2, inp):
        if inp % i == 0:
            print(inp, 'Is not prime number')
            break
    print(inp, 'Is prime number')
