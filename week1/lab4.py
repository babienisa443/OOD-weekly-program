
def odd_list(numbers, odds):
    if len(numbers) == 0:
        return
    v = numbers.pop()
    if v % 2 == 1:
        odds.append(v)
    odd_list(numbers, odds)

odds = []
    
    

print(" ***Function Odd List***")
ls = [int(e)
for e in input("Enter list numbers : ").split()]
print("Input list : " , ls )
odd_list(ls,odds)
new=[odds[i] for i in range(len(odds)-1,-1,-1)]
print("Output list : ", new)
