def one(sensorA,sensorB,size):
    sum=0
    for i in range(size):
        sum+= abs(sensorA[i]-sensorB[i])
    return sum

def onee(sensorA,sensorB,size):
    if size==0: return 0
    lastElementSum=abs(sensorA[size-1]-sensorB[size-1])
    sum=onee(sensorA,sensorB,size-1)+lastElementSum
    return sum

def fibonacci(a,b,num):
    sum=0
    for i in range(num):
        print(a,'+',b,'=',a+b)
        sum=a+b
        a=b
        b=sum
    return sum
def fibonaccii(a,b,num):
    if num==0:
        return 0
    lastnum=a+b
    sum=fibonacci(a,b,num-1)+lastnum
    return sum

if __name__== '__main__':
    #a=onee([15,-4,56,10,-23],[14,-9,56,14,-23],5)
    a=fibonaccii(0,1,5)
    print(a)