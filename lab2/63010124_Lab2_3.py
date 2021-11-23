'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 2	item : 3	ครั้งที่ : 0002
 * Assigned : Tuesday 24th of August 2021 08:46:15 PM --> Submission : Tuesday 24th of August 2021 08:55:36 PM	
 * Elapsed time : 9 minutes.
 * filename : 3.py
'''
def mod_position(arr, s):
    ans=[]
    for i in range(len(arr)+1):
        if i%int(s) == 0:
            ans.append(arr[i-1])
    #pop first letter cause index 0
    ans.pop(0)
    return ans 

print('*** Mod Position ***')
arr,s=input("Enter Input : ").split(',')
print(mod_position(arr,s))