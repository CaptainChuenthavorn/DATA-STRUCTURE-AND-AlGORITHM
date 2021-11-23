'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 1	item : 1	ครั้งที่ : 0003
 * Assigned : Wednesday 11th of August 2021 10:22:47 AM --> Submission : Wednesday 11th of August 2021 09:42:41 PM	
 * Elapsed time : 679 minutes.
 * filename : 1-1.py
'''
print('*** Rabbit & Turtle ***')
print('Enter Input : ',end='')
d,Vr,Vt,Vf = [float(x) for x in input().split()]
Vtf=(Vt/Vr)
Sr=d/(Vtf-1)
St=Sr+d
t=Sr/Vr
Sf=Vf*t
print("{0:.2f}".format(Sf))