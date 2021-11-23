'''
 * กลุ่มที่  : 21010001
 * 63010124 จักรภัทรณ์ ชื่นถาวร
 * chapter : 1	item : 4	ครั้งที่ : 0004
 * Assigned : Wednesday 11th of August 2021 10:43:30 AM --> Submission : Wednesday 11th of August 2021 12:12:13 PM	
 * Elapsed time : 88 minutes.
 * filename : 1-4.py
'''
def num_grid(lst):

    '''
    [i-1][j-1] , [i-1][j] , [i-1][j+1]
    [i][j-1]   , [i][j]   , [i][j+1]
    [i+1][j-1] , [i+1][j] , [i+1][j+1]    
    '''
    #Code Here
    #set zero
    for i,x in enumerate(lst):
        for j,y in enumerate(lst[i]):  
            if y == '-':
                lst[i][j]=0   
            
    #check num
    for i,x in enumerate(lst):
        for j,y in enumerate(lst[i]):
            '''#Edition 3 
            
            for m in range(i-1,i+2):
                    for n in range(j-1,j+2):
                        try:
                            if lst[m][n] == '#':
                                lst[i][j]+=1
                                
                        except:
                            pass'''
                            
            #edition#2
            if y == '#':
                for m in range(max(0,i-1),min(len(lst)-1,i+1)+1):
                    for n in range(max(0,j-1),min(len(lst)-1,j+1)+1):
                        if lst[m][n]=='#':
                            pass
                        else:
                            
                            lst[m][n]+=1 
                        
               
                '''Edition#1
                if lst[i-1][j-1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i-1][j-1]+=1
                elif lst[i-1][j-1]=='#':
                    pass
                else:
                    lst[i-1][j-1]=1
                #2
                if lst[i-1][j] in [1,2,3,4,5,6,7,8,9]:
                    lst[i-1][j]=+1
                elif lst[i-1][j]=='#':
                    pass
                else:
                    lst[i-1][j]=1
                #3
                if lst[i-1][j+1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i-1][j+1]=+1
                elif lst[i-1][j+1]=='#':
                    pass
                else:
                    lst[i-1][j+1]=1
                #4
                if lst[i][j-1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i][j-1]=+1
                elif lst[i][j-1]=='#':
                    pass
                else:
                    lst[i][j-1]=1
                #5
                if lst[i][j+1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i][j+1]=+1
                elif lst[i][j+1]=='#':
                    pass
                else:
                    lst[i][j+1]=1
                #6
                if lst[i+1][j-1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i+1][j-1]=+1
                elif lst[i+1][j-1]=='#':
                    pass
                else:
                    lst[i+1][j-1]=1
                #7
                if lst[i+1][j] in [1,2,3,4,5,6,7,8,9]:
                    lst[i+1][j]=+1
                elif lst[i+1][j]=='#':
                    pass
                else:
                    lst[i+1][j]=1
                #8
                if lst[i+1][j+1] in [1,2,3,4,5,6,7,8,9]:
                    lst[i+1][j+1]=+1
                elif lst[i+1][j+1]=='#':
                    pass
                else:
                    lst[i+1][j+1]=1'''
        
    for i,x in enumerate(lst):
        for j,y in enumerate(lst[i]):  
            if y in [0,1,2,3,4,5,6]:
            
                lst[i][j]=str(y)   
            
    return lst


'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''
print('*** Minesweeper ***')
print('Enter input(5x5) : ',end='')
lst_input = []

input_list = input().split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")