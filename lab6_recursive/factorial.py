def Fac(n):#n>=0
    if n==0 or n==1:#base case
        return 1
    else:#recursive case
        return Fac(n-1)*n