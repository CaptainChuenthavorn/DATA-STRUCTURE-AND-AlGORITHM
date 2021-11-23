'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 6	item : 1	ครั้งที่ : 0001
 * Assigned : Thursday 16th of September 2021 11:26:28 AM --> Submission : Thursday 16th of September 2021 11:01:09 PM	
 * Elapsed time : 694 minutes.
 * filename : 1.py
'''
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

raw = int(input('Enter Number : '))
print(f'{raw}! = {fac(raw)}')