def bbsort(data):
    for i in range(len(data)-1):
        swap=False
        last_Swap='None'
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                swap=True
                last_Swap = inp[j+1]
        if not swap:
            print("last step : {} move[{}]".format(data,last_Swap))
            return 
        else:
            if i==len(data):
                print("last step : {} move[{}]".format(data,last_Swap))
            else:
                print("{} step : {} move[{}]".format(i+1,data,last_Swap))
    return
inp=list(map(int,input("Enter Input : ").split()))
bbsort(inp)


        
            
                