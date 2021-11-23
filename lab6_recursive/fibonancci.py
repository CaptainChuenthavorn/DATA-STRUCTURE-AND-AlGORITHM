'''
Fn=F(n-2) + F(n-1)
'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return fib(n-2)+fib(n-1)
def fib_iter(n):
    if n==0 or n==1:
        return n
    else:
        lo,hi =0,1
        for i in range(2,n+1):
            new = hi+lo
            lo=hi
            hi=new
        return new
def fibLowHi(n,low,high):
    if n==1:
        return low+high
    
#memorize + recursive
memoized = {} 
def fibMemo(n,time):
    time+=1
    if n<=1:
        return n
    if n not in memoized:
        print('im in na')
        memoized[n] = fib(n-2)+fib(n-1)
        print(memoized)
    return memoized,time

a,t=fibMemo(20,0)
print(a)
print('time',t)
