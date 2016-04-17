import sys

cases = []

def numGold(tiles):
    return tiles[0].count('1')

with open(sys.argv[1]) as f:
    for i in range(int(f.readline())):
        k,c,s = [int(x) for x in f.readline().split()]
        
        seq = [bin(x)[2:].zfill(k) for x in range(2**k)]
        art = seq
        for j in range(c):
            nxt = []
            for v,a in enumerate(art,1):
                frac = ''
                for t in a:
                    if(t=='0'): frac+=a
                    else: frac+='1'*k
                
                nxt.append(frac)
            art = nxt
        
        print(art)
        tiles = [[x,n] for n,x in enumerate(zip(*art))]
        print(tiles)
        print('\n')
        
            
        
        
        # ans = 'Case #'+str(i+1)+': '+str(     )+'\n'
        # print(ans)
        # cases.append(ans)

with open(sys.argv[2],'w+') as g:
    g.writelines(cases)
#             