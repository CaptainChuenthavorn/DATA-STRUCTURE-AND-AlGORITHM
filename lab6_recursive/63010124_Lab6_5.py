'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 6	item : 5	ครั้งที่ : 0002
 * Assigned : Thursday 16th of September 2021 11:26:36 AM --> Submission : Friday 17th of September 2021 09:44:31 PM	
 * Elapsed time : 2057 minutes.
 * filename : 5.py
'''
'''
Enter Input : 7
______#
_____##
____###
___####
__#####
_######
#######
'''
def pattern(max,n):
    if max == 0:
        return print('Not Draw!')
    if n==0:
        return
    #ถ้าเป็นลบ
    elif n<0:
        pattern(max,n+1)
        print('_'*(abs(n)-1)+'#'*(abs(max-n)+1))
    #ถ้าเป็นบวก
    else:
        pattern(max,n-1)
        print('_'*(max-n)+'#'*n)
n = int(input('Enter Input : '))
pattern(n,n)