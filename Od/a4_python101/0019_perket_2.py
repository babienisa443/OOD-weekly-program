import math


def Perget(sour, bitter):
    sum_sour = 1
    sum_bitter = 0
    for i in sour:
        sum_sour *= i
    for i in bitter:
        sum_bitter += i
    return abs(sum_sour-sum_bitter)


inp = int(input())


def caller():
    lowest = math.inf
    ingredients = []
    for _ in range(inp):
        S, B = map(int, input().split())
        ingredients.append([S, B])
    if (len(ingredients) == 1):
        print(Perget([ingredients[0][0]], [ingredients[0][1]]))
        return

    def worker(ingredients, currentIngredients):
        if (len(ingredients) == 0):
            return
        for index, ingredient in enumerate(ingredients):
            nonlocal lowest
            sour = []
            bitter = []
            for i in currentIngredients:
                [S, B] = i
                sour.append(S)
                bitter.append(B)
            lowest = min(Perget(sour, bitter), lowest)
            worker(ingredients[:index] + ingredients[index+1:],
                   [*currentIngredients, ingredient])
    worker(ingredients, [])
    print(lowest)


caller()
