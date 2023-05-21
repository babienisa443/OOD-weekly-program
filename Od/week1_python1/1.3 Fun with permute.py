def swap(arr):
    ls = []
    ls.append(arr.copy())
    for i in range(len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        ls.append(arr.copy())
    return ls


print('*** Fun with permute ***')
inp = list(map(int, input('input : ').split(',')))
print(f"Original Cofllection:  {inp}")

temp = [[inp[0]]]

for i in range(1, len(inp)):
    ans = []
    for j in temp:
        #  [swap , ans]
        ans = [*ans, *swap([inp[i], *j])]
    temp = ans
print(f"Collection of distinct numbers:\n {temp}")
