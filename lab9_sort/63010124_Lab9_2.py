#6 3 -2 5 -8 2 -2
lst = [int(x) for x in input("Enter Input : ").split()]
for i in range(len(lst)-1):
    
    #ให้เริ่มiตัวใหม่ ถ้าเจอจน.ลบ
    if lst[i] < 0:
        continue
    #ช่วงเทียบ
    min_idx = 0
    for j in range(0,len(lst)-1):
        if lst[j] > lst[j+1]:
            if lst[j+1] < 0:
                if j+2 < len(lst):
                    if lst[j]>lst[j+2]:
                        lst[j],lst[j+2]=lst[j+2],lst[j]
                        #print(f'we swap {lst[j+2]} - {lst[j]} special case')
            else:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                #print(f'we swap {lst[j+1]} - {lst[j]}')
        

print(*lst)
