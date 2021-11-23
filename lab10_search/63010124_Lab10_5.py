#6 2 4 3 7/3
def minBox(lst,numbox):
    left = max(lst)
    right = sum(lst)
    while left <= right:
        box_weight = (left+right)//2
        box_count = 0
        i=0
        while i<len(lst):
            weight = 0
            while i < len(lst) and weight + lst[i] <=box_weight:
                weight +=lst[i]
                i+=1
            box_count+=1

        if box_count<=numbox: #ได้กล่องน้อยกว่าที่คิด
            right = box_weight-1
        else: # ได้กล่องมากกว่าที่กำหนด
            left = box_weight+1
    
    
    return left # นน.

lst,box = input("Enter Input : ").split('/')
lst=list(map(int,lst.split()))
box = int(box)
print(f"Minimum weigth for {box} box(es) = {minBox(lst, box)}")