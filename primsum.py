import math
import prime

prist = prime.pckr(2,101)

def cops(n):    #COPS - COnsecutive Prime Sum
    cop=[]
    ps = 0
    i=0     #first prime index
    j=0     #last prime index
    while ps != n:
        if prist[j] > n:
            return []
            break
        elif ps < n:      #if ps too small, add new prime
            ps += prist[j]
            cop.append(prist[j])
            j+=1
        elif ps > n:      #if ps too big, subtract first prime
            ps -= prist[i]
            cop.remove(prist[i])
            i+=1
    return cop
            
bg=0
for x in range(0,100):
    if len(cops(x)) > bg:
        bg = x

print(bg,len(cops(bg)), cops(bg))
