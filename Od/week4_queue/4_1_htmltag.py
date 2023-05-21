class Stack :
    def __init__(self,list = None) :
        if list == None :
            self.item = []
        else :
            self.item = list

    def isEmpty(self) : #empty=true
        if self.item == [] :
            return True
        else:
            return False
    def push(self,i) :
        self.item.append(i)
        
    def pop(self) :
        return self.item.pop(-1)
    def size(self) :
        return len(self.item)

def isMatchedHtml(raw):
    S = Stack()
    j = raw.find('<')  #j is index of open
    while j != -1:
        k = raw.find('>', j+1) #find return index
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag) 
        else:
            if S.isEmpty(): 
                return False
            if tag[1:] != S.pop(): 
                return False
        j = raw.find('<' , k+1) 
    return S.isEmpty()

raw = input("Enter HTML content : ")
if isMatchedHtml(raw):
    print ("This is match tag HTML")
else:
    print("This is not match tag HTML")