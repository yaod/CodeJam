#f = open('B-small-attempt0.in','r')
f = open('test.txt','r')
g = open('outputB.txt','w')
n = int(f.readline())
cases = []
count=0

def delete(n) :
    for e in edges:
        if n in e :
            edges.remove(e)

def check(edges,n) :
    c,d=0,[]
    for e in edges :
        if e[0]==n :
            c+=1
            d.append(e[1])
            edges.remove(e)
        if c==0 : return true
        elif c!=2 : return false
        else :
            edges.remove((d[0],n))
            edges.remove((d[1],n))
            return check(edges,d[0]) and check(edges,d[1])

for i in range(n):
    nodes = f.readline()
    edges,queue=[],[]
    for j in range(nodes-1) :
        edges.append(tuple(f.readline().split()))
    for e in edges:
        edges.append((e[1],e[0]))
    queue.append(edges)
    for d in range(n) :
        #if any(any(check(t,r) for r in (z for z in )for t in queue) :
        #    count = d
        #    break
        new = []
        
    g.write(`count`+'\n')
f.close()
g.close()