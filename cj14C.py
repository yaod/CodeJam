def calc(r,c,m):
    s,no = '',[1,2,3,5,7]
    if r==1 or c==1: 
        if r*c<m+2 and m!=0: s = 'Impossible'
        else :
            if r==1 : x=''
            else : x='\n'
            s = 'c'+(r*c-m-1)*(x+'.')+m*(x+'*')
    elif r*c-m in no or r*c-m<=0: s = 'Impossible'
    else :
        t,i=[0]*r,0
        while(m>0 and i<r):
            if i==r-2 :
                if t[i-1]==c and m==1:
                    t[i-1:] = [c-3,2,2]
                    m=0
                else:
                    if m==1:
                        t[i-1]-=1
                        m=2
                    t[i]=m/2
                    m=m/2
            elif m==c-1 :
                t[i] = c-2
                m = 1
            else:
                t[i] = min(c,m)
                m = m-c
            i+=1
        for j in range(r):
            s+=t[j]*'*'+(c-t[j])*'.'+'\n'
        s=s[:len(s)-2]+'c'
    return s

f = open('C-small-attempt1.in','r')
n = int(f.readline())
cases = []
for i in range(n):
    x = f.readline().split()
    y = calc(int(x[0]),int(x[1]),int(x[2]))
    cases.append('Case #'+`i+1`+':\n'+y)
f.close()
g = open('outputC.txt','w')
for z in cases :
    g.write(z+'\n')
g.close()