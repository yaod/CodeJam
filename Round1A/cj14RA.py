import itertools
range = lambda stop: iter(itertools.count().next, stop)

f = open('A-large.in','r')
#f = open('test.txt','r')
g = open('outputA.txt','w')
n = int(f.readline())
cases = []
for i in range(n):
    count = -1
    s = 'Case #'+`i+1`+': '
    t = f.readline().split();
    start = f.readline().split();
    end = f.readline().split();
    sc,ec = {},{}
    for x in start :
        sc[x] = sc.get(x,0)+1
    for y in end :
        ec[y] = ec.get(y,0)+1
    for j in range(2**int(t[1])) :
        k=str(bin(j))[2:].zfill(int(t[1]));
        if all(sc.get(''.join('0' if a == b else '1' for a, b in zip(z,k))) == ec.get(z) for z in ec.keys()) :
            count = str(bin(j)).count('1')
            break;
    if count==-1 : s += 'NOT POSSIBLE'
    else : s += `count`
    g.write(s+'\n')
f.close()
g.close()