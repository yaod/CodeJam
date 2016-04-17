cases = []
with open('B-small-practice.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        if i%2 == 0:
            n = int(line)
        else:
            diners = line.split()
            diners = [int(e) for e in diners]
            if n == 1:
                time = min(1+(diners[0]+1)//2,diners[0])
            else:
                map = {j:diners.count(j) for j in set(diners)}
                time = 0
                plates = sorted(map.keys())
                maxD = plates[len(plates)-1]
                
                if maxD == 9:
                    newD = 6
                    othD = 3
                else:
                    newD = (maxD+1)//2
                    othD = maxD//2
                num = map[maxD]

                if len(plates) == 1: nextD = newD
                else : nextD = max(newD,plates[len(plates)-2])
                
                while maxD > 3 and num+nextD <= maxD:
                    time +=num
                    map[newD] = map.get(newD, 0) + num
                    map[othD] = map.get(othD, 0) + num
                    del map[maxD]
                    plates = sorted(map.keys())
                    maxD = plates[len(plates)-1]
                    nextD = plates[len(plates)-2]
                time += max(plates)
            
            cases.append('Case #'+str(i//2+1)+': '+str(time)+'\n')

with open('B-small-practice.out','w+') as g:
    g.writelines(cases)