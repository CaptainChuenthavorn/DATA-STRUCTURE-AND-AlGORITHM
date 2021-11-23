def numToBase(i,num):
    #ans keep list of base num
    ans=[]
    while num>=1:
        #append R
        ans.append(num%i)
        num = int(num/i)
    ans.reverse()
    return ans
def hbd(age):
    i=1
    for i in range(2,age):
        ans=[]
        x=numToBase(i,age)
        #equal to 20 or 21
        if x == [2,1]:
            ans.append(21)
            ans.append(i)
            return ans
        elif x==[2,0]:
            ans.append(20)
            ans.append(i)
            return ans
   
          

year = input("Enter year : ")
ans = hbd(int(year))
print(f"saimai is just {ans[0]}, in base {ans[1]}!")

