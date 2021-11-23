'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 1	item : 3	ครั้งที่ : 0003
 * Assigned : Wednesday 11th of August 2021 10:38:12 AM --> Submission : Wednesday 11th of August 2021 10:43:21 AM	
 * Elapsed time : 5 minutes.
 * filename : 1-3.py
'''
print(' *** Summation of each digit ***')
print('Enter a positive number : ',end='')
n = input()
print('Summation of each digit =  ',end='')
sum=0
for i in n:
    sum+=int(i)
print(sum)