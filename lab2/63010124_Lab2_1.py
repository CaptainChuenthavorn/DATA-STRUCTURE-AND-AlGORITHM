'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 2	item : 1	ครั้งที่ : 0001
 * Assigned : Tuesday 24th of August 2021 08:30:23 PM --> Submission : Tuesday 24th of August 2021 08:40:54 PM	
 * Elapsed time : 10 minutes.
 * filename : 1.py
'''
def Rshift(num,shift):
    return num>>shift
    ### Enter Your Code Here ###

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))