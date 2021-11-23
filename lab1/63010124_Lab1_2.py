'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 1	item : 2	ครั้งที่ : 0001
 * Assigned : Wednesday 11th of August 2021 10:33:12 AM --> Submission : Wednesday 11th of August 2021 10:37:43 AM	
 * Elapsed time : 4 minutes.
 * filename : 1-2.py
'''
print('*** multiplication or sum ***')
print('Enter num1 num2 : ',end='')
n = [int(x) for x in input().split()]
print('The result is ',end='')
if n[0]*n[1]>1000:
    print(n[0]+n[1])
else:
    print(n[0]*n[1])
