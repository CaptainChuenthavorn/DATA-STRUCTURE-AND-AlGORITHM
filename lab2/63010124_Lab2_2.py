'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 2	item : 2	ครั้งที่ : 0001
 * Assigned : Tuesday 24th of August 2021 08:41:05 PM --> Submission : Wednesday 25th of August 2021 11:09:55 AM	
 * Elapsed time : 868 minutes.
 * filename : 2.py
'''
def weirdSubtract(n,k):
	for i in range(k):
		if n%10==0:
			n/=10
		else:
			n-=1
	return int(n)

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))
