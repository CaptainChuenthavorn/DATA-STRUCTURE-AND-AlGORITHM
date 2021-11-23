def bubblemin(lst):
    #len(lst) -1 เพราะกันindex error
    for first in range(len(lst)-1):
        for i in range(len(lst)-first-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst

def sort_string_by_ascii(data):
    #sort ascii
    data = [str(x) for x in data]
    #print(data)
    #data = [int(x) for ord(x) in data]
    newdata=[]
    for i in data:
        #print(ord(i),i)
        newdata.append(ord(i))
    #print(newdata)
    bubblemin(newdata)
    #print(newdata)
    newdata2=[]
    for i in newdata:
        newdata2.append(chr(i))
    #print(newdata2)
inp = input()
a=sort_string_by_ascii(inp)
print(a)