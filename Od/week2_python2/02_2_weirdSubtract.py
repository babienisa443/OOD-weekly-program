def weirdSubtract(n, k):
    for i in range(k):

        if n % 10 == 0:

            n = n/10
        else:

            n = n-1
    print(int(n))


n, s = input("Enter num and sub : ").split()

weirdSubtract(int(n), int(s))
