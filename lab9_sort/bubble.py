#bigO(n^2) 1+2+3+...+(n*2)+(n-1)
def bubble(lst):
    for last in range(len(lst)-1,-1,-1):
        for i in range(last):
                if lst[i] < lst[i+1]:
                    lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst

def bubblemin(lst):
    #len(lst) -1 เพราะกันindex error
    for first in range(len(lst)-1):
        for i in range(len(lst)-first-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
def selection(lst):
    for first in range(len(lst)-1):
        biggest = lst[0]
        biggest_i  = 0
        for i in range(len(lst)-1-first):
            
            if lst[i] > biggest:
                biggest=lst[i]
                biggest_i=i
        if lst[biggest_i] >lst[len(lst)-1-first]:
            lst[biggest_i],lst[len(lst)-1-first]=lst[len(lst)-1-first],lst[biggest_i]
        
        print(f'we swap {lst[biggest_i]} {lst[len(lst)-1-first]} ')
    return lst

lst=[5,6,2,3,0,1,4]
a=bubblemin(lst)
print(a)
b=selection(lst)
print(b)