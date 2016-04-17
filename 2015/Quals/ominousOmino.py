cases = []
with open('D-large.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        x,r,c = [int(s) for s in line.split()]
        if x<7 and r*c%x == 0 and min(r,c) >= 1+(x+1)//2:
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'
        cases.append('Case #'+str(i+1)+': '+winner+'\n')

with open('D-large.out','w+') as g:
    g.writelines(cases)