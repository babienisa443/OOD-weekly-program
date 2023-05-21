def selectSort(arr, i, j, max_index):
    
    if j == -1:
        # swap 1 <-> 2 : [1, 2, 3, 4, 5]
        # Swap
        if i != max_index:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            print("swap", arr[max_index], "<->", arr[i], ":", arr)
        
        i = i-1
        j = i-1
        max_index = i
        
    if i==0:
        return
    
    if arr[j] > arr[max_index]:
        max_index = j
        
   
    selectSort(arr, i, j-1, max_index)


inp = list(map(int, input("Enter Input : ").split(" ")))
    
# arr = [40 20 30 10 50]
n = len(inp)
#                i   j  max_index
selectSort(inp, n-1, n-2, n-1)
print(inp)