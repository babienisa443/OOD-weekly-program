class Queue :
    def __init__(self,item=None):
        if item == None :
            self.item = []
        else :
            self.item = item
    def enQueue(self,item):
        self.item.append(item)
    def deQueue(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.item == []
Em1,Em2 = input('Enter Input : ').split('/')
a = Em1.split(',')
b = Em2.split(',')
empQueue = [item.split(' ') for item in a]#ชื่อแผนก
empStaffQueue = [item.split(' ') for item in b]#แผนกที่ทำการอินพุต
dictId = {}
for i in empQueue :
    dictId[i[1]] = i[0]

dictQueue = {}
for i in empStaffQueue : 
    if i[0] == 'E':
        if dictQueue.get(dictId[i[1]]) is None:
            dictQueue[dictId[i[1]]] = Queue()
        dictQueue[dictId[i[1]]].enQueue(i[1])
    else :
        if len(dictQueue) == 0 :
            print('Empty')
        else :
            key = list(dictQueue.keys())
            print(dictQueue[key[0]].deQueue())
            if dictQueue[key[0]].isEmpty():
                del dictQueue[key[0]]