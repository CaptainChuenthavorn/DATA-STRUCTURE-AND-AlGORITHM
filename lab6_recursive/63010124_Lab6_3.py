'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 6	item : 3	ครั้งที่ : 0004
 * Assigned : Thursday 16th of September 2021 11:26:32 AM --> Submission : Saturday 18th of September 2021 11:35:06 AM	
 * Elapsed time : 2888 minutes.
 * filename : 3.py
'''
'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11
e.g.
Enter Number : 4
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
'''
def num(decnum):
    if decnum==0:
        return 0
    else:
        return decnum%2+10 * num(decnum//2)
def big_recur(decimal,bit):
    #negative num
    if decimal<0:
        return print('Only Positive & Zero Number ! ! !')
    #if input==0
    if decimal==0 and bit==0:
        return print(0)
    if decimal==0:
        return 0
    else:
        #พิม  000 ตัวแรก
        if decimal==bit:
            print('0'*bit)
        big_recur(decimal-1,bit)
        ans = num(decimal)
        #เติมบิท0ข้างหน้า
        if len(str(ans))!= bit:
            print('0'*(bit-len(str(ans)))+str(ans))
        #กรณีbitอยู่เต็มแล้ว
        else:
            print(ans)
decimal_number = int(input('Enter Number : '))
#print(num(decimal_number))
bit = decimal_number
big_recur(2**decimal_number-1,bit)
 
