#import random
#import numpy
f = open('C-small-practice.in','r')
#f = open('test.txt','r')
g = open('outputC.txt','w')
n = int(f.readline())
cases = []
for i in range(n):
    s = 'Case #'+`i+1`+': '
    m=int(f.readline())
    lst=f.readline().split()
    lst=map(int,lst)
    first,middle,last=sum(lst[:m/3]),sum(lst[m/3:2*m/3]),sum(lst[2*m/3:])
    if first+10<middle and middle+10<last :
        s+='BAD'
    else : s+='GOOD'
    g.write(s+'\n')
f.close()
g.close()

def good(n) :
    a=range(n)
    for k in range(n):
        p=random.randrange(k,n)
        temp = a[k]
        a[k] = a[p]
        a[p] = temp
    return a

def bad(n) :
    a=range(n)
    for k in range(n):
        p=random.randrange(0,n)
        temp = a[k]
        a[k] = a[p]
        a[p] = temp
    return a

#goodlist = [0] * 10
#badlist  = [0] * 10

#for i in range(100000) :
#    g=good(10)
#    b=bad(10)
#    for j in range(10) :
#        goodlist[j]+=g[j]
#        badlist[j] +=b[j]

#print "good: ",numpy.std(goodlist)/100000,"\nbad: ",numpy.std(badlist)/100000
