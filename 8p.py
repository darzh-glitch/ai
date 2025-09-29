from collections import deque

def solve(start, goal='123456780'):
    q, seen = deque([(start, [])]), {start}
    for state, path in iter(q.popleft, None):
        if state == goal: return path+[state]
        i = state.index('0')
        for d in (-3,3,-1,1):
            j=i+d
            if 0<=j<9 and not(i%3==0 and d==-1) and not(i%3==2 and d==1):
                l=list(state); l[i],l[j]=l[j],l[i]; n=''.join(l)
                if n not in seen: seen|={n}; q.append((n,path+[state]))

puzzle=input("Enter 9-digit puzzle (0 = blank): ")
if len(puzzle)==9 and set(puzzle)==set('012345678'):
    steps=solve(puzzle)
    for s in steps: print(s[0:3],s[3:6],s[6:9],'',sep='\n')
    print("Total moves:",len(steps)-1)
else: print("Invalid input!")

