'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 6	item : 2	ครั้งที่ : 0003
 * Assigned : Thursday 16th of September 2021 11:26:30 AM --> Submission : Friday 17th of September 2021 03:02:20 PM	
 * Elapsed time : 1655 minutes.
 * filename : 2.py
'''
def palindrome_check(s,first_index,last_index):
    #ถ้ามีแค่ 1 หรือ 0 ตัว
    if len(s) == 0 or len(s) == 1:
        return True
    #ถ้าตัวหน้ากะท้ายไม่เหมือนกัน
    if s[first_index] != s[last_index]:
        return False
    #กัน index out of range
    if first_index< last_index+1:
        return palindrome_check(s,first_index+1,last_index-1)
    
    return True
    
        


s=input('Enter Input : ')
tempS = s
s=s.lower()
ans=palindrome_check(s,0,len(s)-1)
if ans:
    print(f"'{tempS}' is palindrome")
else:
    print(f"'{tempS}' is not palindrome")