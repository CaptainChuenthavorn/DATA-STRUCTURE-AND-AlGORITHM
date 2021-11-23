'''
name, wins, loss, draws, scored, conceded 
'''
def calScore(lst):
    for i in range(1,len(lst)):
        lst[i] = int(lst[i])
    score = lst[1]*3+ 0*lst[2] + 1*lst[3]
    gd = lst[4]-lst[5]
    ans=[score,gd]
    return ans
    
def sort(lst):
    ans=[]
    ans.append(calScore(lst))
    return ans

def levelScore(lst,team):
    for first in range(len(lst)-1):
        for i in range(len(lst)-first-1):
            if lst[i][0] < lst[i+1][0]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                team[i],team[i+1]=team[i+1],team[i]
            #if point equal check gd
            if lst[i][0] == lst[i+1][0]:
                if lst[i][1] < lst[i+1][1]:
                    lst[i],lst[i+1]=lst[i+1],lst[i]
                    team[i],team[i+1]=team[i+1],team[i]
    ans = []
    for j in range(len(lst)):
        temp=[team[j][0],lst[j][0][0],lst[j][0][1]]
        ans.append(temp)
        
    return ans
inp=input('Enter Input : ').split('/')
team=[]
for i in inp:
    team.append(i.split(','))
score=[]
for i in team:
    score.append(sort(i))
ans = levelScore(score,team)
print('== results ==')
for i in range(len(ans)):
    print(f"['{ans[i][0]}', {'{'}'points': {ans[i][1]}{'}'}, {'{'}'gd': {ans[i][2]}{'}'}]")
    #print(f"{ans}{{}}")