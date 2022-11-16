
def sort(inp):
    for i in range(0, len(inp)-1):
        swap = False
        last_Swap = "None"
        for j in range(0, len(inp)-i-1):
            if inp[j] > inp[j+1]:
                inp[j], inp[j+1] = inp[j+1], inp[j]
                swap = True
                last_Swap = inp[j+1]
        if not swap: #กรณีเรียงมาเเล้ว เช่น 1 2 3 4 5
            print("last step : {} move[{}]".format(inp, last_Swap))
            return
        else:
            if i == len(inp)-2:
                print("last step : {} move[{}]".format(inp, last_Swap))
            else: #ปกติที่ยังswap อยู่
                print("{} step : {} move[{}]".format(i+1, inp, last_Swap))
    return
data = list(map(int ,input("Enter Input : ").split()))
sort(data)


