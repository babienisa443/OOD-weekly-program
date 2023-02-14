class funString():
    string=""
    def __init__(self,string = ""):
        self.string=string
        

    def __str__(self):

        return self.string

    def size(self) :
      counter=0
      for i in self.string:
            counter+=1
      return counter
            
        ### Enter Your Code Here ###

    def changeSize(self):
        
        return self.string.swapcase()
        ### Enter Your Code Here ###

    def reverse(self):
         str = ""
         for i in self.string:
            str = i + str
         return str
        ### Enter Your Code Here ###

    def deleteSame(self):
        list=[]
        #list.append(self.string)
        for i in self.string:
            if i not in list:
                list+=i
        return "".join(list)
            
       ### Enter Your Code Here ###



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())