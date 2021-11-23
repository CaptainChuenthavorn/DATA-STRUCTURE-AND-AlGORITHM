class funString():

    def __init__(self,str1):
        self.str1 = str1
        

    def __str__(self):
        pass
        ### Enter Your Code Here ###

    def size(self) :

        ### Enter Your Code Here ###
        return len(self.str1)

    def changeSize(self):
        ans=[]
        for i in self.str1:
            if i.isupper():
                n=ord(i)
                ans.append(chr(n+32))
            else:
                n=ord(i)
                ans.append(chr(n-32))
        return ''.join(ans)

    def reverse(self):
        return self.str1[::-1]
        

    def deleteSame(self):
        set=[]
        for c in self.str1:
            if c in set:
                pass
            else :
                set.append(c)
        return ''.join(set)

       



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())