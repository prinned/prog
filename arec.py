import prime

def a(n):
    if n ==1:
        return 1
    else:
        return 6*(a(n-1)**2) +10*(a(n-1)) + 3

def b(x,y,z):
    ba = 0
    for p in prime.pckr(x+y+1,x):       #prime.pckr used
        ba += a(z) % p
    return(ba)
    
while 1==1:
    x=int(input("enter: "))
    y=int(input("enter: "))
    z=int(input("enter: "))
    print(b(x,y,z))

