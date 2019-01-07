import math

def cvr(l,b,h):
    return 2*l*b + 2*l*h + 2*b*h
def rvc(n):
    c=0
    k=[]
    for l in range(1,n//4):
        for b in range(1,n//4):
            for h in range(1,n//4):
                if cvr(l,b,h)==n:
                    c+=1
                    k.append({l,b,h})
    return [c,set(k)]

while 1==1:
    x=int(input(": "))
    print(rvc(x))
