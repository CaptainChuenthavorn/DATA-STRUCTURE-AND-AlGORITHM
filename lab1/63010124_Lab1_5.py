'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 1	item : 5	ครั้งที่ : 0004
 * Assigned : Wednesdax 11th of August 2021 11:45:39 AM --> Submission : Thursdax 12th of August 2021 12:11:14 PM	
 * Elapsed time : 1465 minutes.
 * filename : 1-5.px
'''
print('Enter Input : ',end='')
i =int(input())
lst=[]
#6,8,10,...
n = 2*(i+2) 
for y in range(n):
    for x in range(n):
        #in middle of xin xang bottom
        if y>(n/2) and y<n-1 and x<n/2-1 and x!=0:
            print('+',end='')
        #in middle of xin xang top
        elif y>0 and y<(n/2)-1 and x>n/2 and x!=n-1:
            print('#',end='')
        #dot left top
        elif y+x <= i:
            print('.',end='')
        #dot right bottom
        elif y+x >= (2*n)-i-2:
            print('.',end='')
        #col +
        elif x>=n/2:
            print('+',end='')
        #col #
        elif x<n/2:
            print('#',end='')
    print()