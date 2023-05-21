

def Counter(text, stop):
    sum = 0
    for i in text:
        if i == stop:
            return sum
        else:
            sum += 1
    return sum


text, stop = input().split(',')
c = Counter(text, stop)
print(c)
