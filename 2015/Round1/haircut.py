from functools import reduce

cases = []
with open('B-small-attempt1.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        if i%2 == 0:
            b,n = [int(a) for a in line.split()]
        else:
            barb = [int(j) for j in line.split()]
            if all(z==barb[0] for z in barb):
                m = n % b
                if m == 0: m = b
            else:
                mult = reduce(lambda x, y: x * y, barb, 1)
                nsum = reduce(lambda x, y: int(mult/y + x), barb, 0)
                cuts = [0]*b
                if n%nsum == 0: r = nsum
                else: r = n%nsum

                for k in range(1,r):
                    m = cuts.index(min(cuts))
                    cuts[m]+=barb[m]
                m = cuts.index(min(cuts))+1
                
            cases.append('Case #'+str(i//2+1)+': '+str(m)+'\n')

with open('B-small-attempt1.out','w+') as g:
    g.writelines(cases)